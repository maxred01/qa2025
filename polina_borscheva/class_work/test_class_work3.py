import requests
import pytest


@pytest.mark.parametrize('data_id, data_title, data_dueDate, data_completed, status_code', [
    (100, '4334434', "2026-05-12T16:43:35.873Z", True, 200),
    ('1871863', 645, '', False, 400),
     ('', '', 45675648, None, 400),
    ('1871863', '3435545', True, True, 400),
    (None, None, None, None, 400)
])
@pytest.mark.skip("Пропускаем")
def test_api_v1_activities(data_id, data_title, data_dueDate, data_completed, status_code):
    URL = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

    playlaod = {
        "id": data_id,
        "title": data_title,
        "dueDate": data_dueDate,
        "completed": data_completed
    }

    response = requests.post(url=URL,
                             json=playlaod)

    response_json = response.json()

    assert response.status_code == status_code

    assert response_json['id'] == data_id
    assert response_json['title'] == data_title
    assert response_json['dueDate'] == data_dueDate
    assert response_json['completed'] == data_completed