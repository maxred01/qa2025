import requests
import pytest

@pytest.mark.parametrize("data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code",[
                             (5, "test", "string", 0, "string", "2026-05-13T18:35:43.071Z", 200),
                             ("123424", 223535, '', False, 400, "wrwrwff", 201),
                             ('', '', 223535, None, 400, "dwrfwf", "wfwefweg"),
                             (" 32482942 ", " 32482942 ", True, True, 400, " ", " "),
                             (None, None, None, None, 400, 9242, 2424),
                         ])
# @pytest.mark.skip("Пропускаем")
def test_api_v1_books_post(data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code):
    URL = 'https://fakerestapi.azurewebsites.net/api/v1/Books'


    payload = {
      "id": data_id,
      "title": data_title,
      "description": data_description,
      "pageCount": data_pageCount,
      "excerpt": data_excerpt,
      "publishDate": data_publishDate
    }

    response = requests.post(url=URL,
                             json=payload)

    response_json = response.json()
    assert response.status_code == status_code

    assert response_json['id'] == data_id
    assert response_json['title'] == data_title
    assert response_json['description'] == data_description
    assert response_json['pageCount'] == data_pageCount
    assert response_json['excerpt'] == data_excerpt
    assert response_json['publishDate'] == data_publishDate


@pytest.mark.parametrize("data_id, status_code",[
                             (1, 200),
                             ("123424", 201),
                             (None, True),
                             ("@", " "),
                             (-1, "sfgergerg"),
                         ])

def test_api_v1_books_get (data_id, status_code):
    URL = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'


    response = requests.get(url=URL)

    response_json = response.json()
    assert response.status_code == status_code

    assert response_json['id'] == data_id
    assert type(response_json['title']) == str
    assert type(response_json['description']) == str
    assert type(response_json['pageCount']) == int
    assert type(response_json['excerpt']) == str

@pytest.mark.parametrize("data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code",[
                             (0, "string", "string", 0, "string", "2026-05-17T08:25:29.171Z", 200),
                             ("123424", 223535, '', False, 400, "wrwrwff", 201),
                             ('', '', 223535, None, 400, "dwrfwf", "wfwefweg"),
                             (" 32482942 ", " 32482942 ", True, True, 400, " ", " "),
                             (None, None, None, None, 400, 9242, 2424),
                         ])

def test_api_v1_books_put(data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code):
    URL = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'


    payload = {
      "id": data_id,
      "title": data_title,
      "description": data_description,
      "pageCount": data_pageCount,
      "excerpt": data_excerpt,
      "publishDate": data_publishDate
    }

    response = requests.put(url=URL,
                             json=payload)

    response_json = response.json()
    assert response.status_code == status_code

    assert response_json['id'] == data_id
    assert response_json['title'] == data_title
    assert response_json['description'] == data_description
    assert response_json['pageCount'] == data_pageCount
    assert response_json['excerpt'] == data_excerpt
    assert response_json['publishDate'] == data_publishDate

@pytest.mark.parametrize("data_id, status_code",[
                             (1, 200),
                             ("123424", 201),
                             (None, True),
                             ("@", " "),
                             (-1, "sfgergerg"),
                         ])

def test_api_v1_books_delete (data_id, status_code):
    URL = f'https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}'


    response = requests.delete(url=URL)

    assert response.status_code == status_code
