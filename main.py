import pytest
import requests
import random

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1/Books"

def create_book_payload(title="TestTitle", description="TestDescription", page_count=100, excerpt="Excerpt", publish_date="2020-01-01T00:00:00.000Z"):
    return {
        "id": random.randint(10000, 99999),
        "title": title,
        "description": description,
        "pageCount": page_count,
        "excerpt": excerpt,
        "publishDate": publish_date
    }

@pytest.fixture
def new_book():
    payload = create_book_payload()
    r = requests.post(BASE_URL, json=payload)
    assert r.status_code == 200 or r.status_code == 201
    return r.json()

@pytest.mark.parametrize(
    "field, value, expected_type",
    [
        ("title", "Sample Book", str),
        ("description", "A desc", str),
        ("pageCount", 56, int),
        ("excerpt", "Some text", str),
        ("publishDate", "2020-01-01T00:00:00.000Z", str),
    ]
)
def test_post_book_success(field, value, expected_type):
    payload = create_book_payload()
    payload[field] = value
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code in [200, 201]
    data = response.json()
    assert field in data
    assert data[field] == value
    assert isinstance(data[field], expected_type)

@pytest.mark.parametrize(
    "missing_field",
    ["title", "description", "pageCount", "excerpt", "publishDate"]
)
def test_post_book_missing_fields(missing_field):
    payload = create_book_payload()
    payload.pop(missing_field)
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code in [400, 500] or "error" in response.text.lower()

def test_get_book_success(new_book):
    book_id = new_book["id"]
    response = requests.get(f"{BASE_URL}/{book_id}")
    assert response.status_code == 200
    data = response.json()
    for key, type_ in [
        ("id", int),
        ("title", str),
        ("description", str),
        ("pageCount", int),
        ("excerpt", str),
        ("publishDate", str)
    ]:
        assert key in data
        assert isinstance(data[key], type_)

def test_get_book_not_found():
    response = requests.get(f"{BASE_URL}/99999999")
    assert response.status_code == 404

def test_put_book_success(new_book):
    book_id = new_book["id"]
    updated_data = dict(new_book)
    updated_data["title"] = "Updated Title"
    r = requests.put(f"{BASE_URL}/{book_id}", json=updated_data)
    assert r.status_code == 200
    data = r.json()
    assert data["title"] == "Updated Title"


def test_put_book_not_found():
    fake_id = 77777777
    updated_data = create_book_payload()
    r = requests.put(f"{BASE_URL}/{fake_id}", json=updated_data)
    assert r.status_code in [404, 500]

def test_delete_book_success(new_book):
    book_id = new_book["id"]
    r = requests.delete(f"{BASE_URL}/{book_id}")
    assert r.status_code == 200 or r.status_code == 204
    # Проверка, что книга реально удалена
    r2 = requests.get(f"{BASE_URL}/{book_id}")
    assert r2.status_code == 404

def test_delete_book_not_found():
    r = requests.delete(f"{BASE_URL}/99999999")
    assert r.status_code == 404