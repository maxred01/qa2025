import requests
import pytest


@pytest.mark.parametrize('data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code', [
    (100, '4334434', 'gf', 67, 'hello ken', "2026-05-12T16:43:35.873Z", 200),
    (89, '1871863', 645, '', True,  False, 400),
    ('', '', 2342345, True, 'ss', None, 400),
    ('1871863', 0, 9, '3435545', True, True, 400),
    (None, None, None, None, None, None, 400)
])
def test_api_v1_books(data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code):
    URL = "https://fakerestapi.azurewebsites.net/api/v1/Books"

    playlaod = {
        "id": data_id,
        "title": data_title,
        "description": data_description,
        "pageCount": data_pageCount,
        "excerpt": data_excerpt,
        "publishDate": data_publishDate,

    }

    response = requests.post(url=URL,
                             json=playlaod)

    response_json = response.json()

    assert response.status_code == status_code

    assert response_json['id'] == data_id
    assert response_json['title'] == data_title
    assert response_json['description'] == data_description
    assert response_json['pageCount'] == data_pageCount
    assert response_json['excerpt'] == data_excerpt
    assert response_json['publishDate'] == data_publishDate
])

def test_api_v1_books(data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code):
    url = "https://fakerestapi.azurewebsites.net/api/v1/Books/5"

    params = {'id': 5}
    response = requests.get(url=url, params=params, json=playlaod)


    response_json = response.json()

    assert response.status_code == 200, f'Неверный статус код. Ожидался 200, получен {response.status_code}'
    assert response_json['id'], f'Параметр "id" отсутствует в ответе'
    assert response_json['title'], f'Параметр "title" отсутствует в ответе'
    assert response_json['description'], f'Параметр "description" отсутствует в ответе'
    assert response_json['pageCount'], f'Параметр "pageCount" отсутствует в ответе'
    assert response_json['excerpt'], f'Параметр "excerpt" отсутствует в ответе'
    assert response_json['publishDate'], f'Параметр "publishDate" отсутствует в ответе'

    assert response_json['id'] == data_id
    assert response_json['title'] == data_title
    assert response_json['description'] == data_description
    assert response_json['pageCount'] == data_pageCount
    assert response_json['excerpt'] == data_excerpt
    assert response_json['publishDate'] == data_publishDate

