import requests
import pytest

@pytest.mark.parametrize('data_id, data_title, data_description, data_page_count, data_excerpt, data_publish_date, status_code',
    [
        (1, "string", "string", 100, "string", "2026-05-18T18:06:56.633Z", 200),
        (None, None, None, None, None, None, 400),
    ]
    )


def test_api_v1_books_post(data_id, data_title, data_description, data_page_count, data_excerpt, data_publish_date, status_code):

    url = 'https://fakerestapi.azurewebsites.net/api/v1/Books'

    payload = {
        "id": data_id,
        "title": data_title,
        "description": data_description,
        "pageCount": data_page_count,
        "excerpt": data_excerpt,
        "publishDate": data_publish_date
    }

    response = requests.post(url=url, json=payload)

    assert response.status_code == status_code

    if status_code == 200:

        data = response.json()

        assert isinstance(data["id"], int)
        assert isinstance(data["title"], str)
        assert isinstance(data["description"], str)
        assert isinstance(data["pageCount"], int)
        assert isinstance(data["excerpt"], str)
        assert isinstance(data["publishDate"], str)

@pytest.mark.parametrize('data_id, status_code',
    [
        (1, 200),
        (-100, 404),
    ]
    )
def test_api_v1_books_get(data_id, status_code):

    url = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'

    response = requests.get(url=url)

    assert response.status_code == status_code

    if status_code == 200:

        data = response.json()

        assert isinstance(data["id"], int)
        assert isinstance(data["title"], str)
        assert isinstance(data["description"], str)
        assert isinstance(data["pageCount"], int)
        assert isinstance(data["excerpt"], str)
        assert isinstance(data["publishDate"], str)


@pytest.mark.parametrize('data_id, data_title, data_description, data_page_count, data_excerpt, data_publish_date, status_code',
    [
        (1, "new title", "new description", 500, "new excerpt", "2026-05-18T18:06:56.633Z", 200),
        (None, None, None, None, None, None, 400),
    ]
)

def test_api_v1_books_put(data_id, data_title, data_description, data_page_count, data_excerpt, data_publish_date, status_code):

    url = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'

    payload = {
        "id": data_id,
        "title": data_title,
        "description": data_description,
        "pageCount": data_page_count,
        "excerpt": data_excerpt,
        "publishDate": data_publish_date
    }

    response = requests.put(url=url, json=payload)

    assert response.status_code == status_code

    if status_code == 200:

        data = response.json()

        assert data["id"] == data_id
        assert data["title"] == data_title
        assert data["description"] == data_description
        assert data["pageCount"] == data_page_count

@pytest.mark.parametrize( 'data_id, status_code',
    [
        (1, 200),
        (-1, 404),
    ]
    )

def test_api_v1_books_delete(data_id, status_code):

    url = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'

    response = requests.delete(url=url)

    assert response.status_code == status_code