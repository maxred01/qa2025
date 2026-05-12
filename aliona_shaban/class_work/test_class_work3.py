import requests
import pytest
@pytest.mark.parametrize('data_id, data_title, data_due_date, data_completed, status_code', [
                             (10, 'string', '2026-05-12T16:47:05.747Z', True, 200),
                             ('123423', 54231, '', False, 400),
                             ('', '', 54231, None, 400),
                             ('56345645', '56345345', True, True, 400),
                             (None, None, None, None, 400),

                         ])
@pytest.mark.skip('Пропускаем')
def test_api_v1_activities(data_id, data_title, data_due_date, data_completed, status_code):
    URL = 'https://fakerestapi.azurewebsites.net/api/v1/Activities/'

    payload = {
     "id": data_id,
     "title": data_title,
     "dueDate": data_due_date,
     "completed": data_completed
    }

    response = requests.post(url=URL,
                             json=payload)

    response_json = response.json()
    assert response.status_code == status_code


    assert response_json['id'] == data_id, f'Неправильное значение'
    assert response_json['title'] is not None, f'Не пустое поле'
    assert response_json['completed'] is True, f'Не булевое значение'

    assert response_json['id'] == data_id
    assert response_json['title'] == data_title
    assert response_json['dueDate'] == data_due_date
    assert response_json['completed'] == data_completed