import requests
import pytest


@pytest.mark.parametrize('data_id', 'data_title', 'data_due_date', 'data_completed', [
                                    (0, "string", '2026-05-12T16:46:08.061Z', True, 200),
                                    ('123423', 54231, '', None, 400),
                                    ('', '', 54321, None, 400),
                                    ('56345345', '56345345', True, True, 400),
                                    (None, None, None, None, 400),
                                ])
@pytest.mark.skip("Пропуск")
def test_api_v1_activities(data_id, data_title, data_due_date, data_completed, status_code):
    url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

    payload = {
        "id": data_id,
        "title": data_title,
        "dueDate": data_due_date,
        "completed": data_completed
    }

    response = requests.post(url=url, json=payload)
    if response.status_code == status_code:
        data = response.json()
        assert data["id"] == data_id
        assert data["title"] == data_title
        assert data["dueDate"] == data_due_date
        assert data["completed"] == data_completed











# assert response.status_code == 200, f'Неверный статус код. Ожидался 200, получен {response.status_code}'
# assert response_json['data'][0]['fact'], f'Параметр "fact" отсутствует в ответе'
# assert response_json['data'][0]['length'], f'Параметр "length" отсутствует в ответе'
# assert isinstance(response_json['data'][0]["fact"], str), f'Параметр "fact" не типа str, а не {type(response_json["fact"])}'
# assert isinstance(response_json['data'][0]["length"], int), f'Параметр "length" не типа int, а не {type(response_json["length"])}'
# assert len(response_json['data'][0]["fact"]) > 0, "Поле пустое"

# assert type(response_json['data'][0]["length"]) == int, "Поле пустое или отсутствует"
# assert response_json['next_page_url'], f'Параметр "next_page_url" отсутствует в ответе'
# assert response_json['path'], f'Параметр "path" отсутствует в ответе'
# assert response_json['per_page'], f'Параметр "per_page" отсутствует в ответе'
# assert response_json['to'], f'Параметр "to" отсутствует в ответе'
# assert response_json['total'], f'Параметр "total" отсутствует в ответе'
