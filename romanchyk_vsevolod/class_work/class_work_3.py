import requests
import pytest
import allure


@allure.feature('Тест с параметризацией')
@allure.story('Тест ручки api/v1/Activities')
@pytest.mark.parametrize('data_id, data_title, data_due_date, data_completed, status_code', [
    (10, "56345345", "2026-05-12T16:43:24.241Z", True, 200),
    ('123423', 54231, '', False, 400),
    ('', '', 54231, None, 400),
    ("56345345", "56345345", True, True, 400),
    (None, None, None, None, 400),

])
@allure.title('Позитивные и негативные проверки с параметризацией')
def test_api_v1_activities(data_id, data_title, data_due_date, data_completed, status_code):
    URL = 'https://fakerestapi.azurewebsites.net/api/v1/Activities/'

    payload = {
        "id": data_id,
        "title": data_title,
        "dueData": data_due_date,
        "completed": data_completed
    }

    response = requests.post(url=URL,
                             json=payload)
    response_json = response.json()

    with allure.step('Конвертация ответа в json'):

        assert response.status_code == status_code

    assert response_json['id'] == data_id
    assert response_json['title'] == data_title
    assert response_json['dueDate'] == data_due_date
    assert response_json['completed'] == data_completed

# assert response.status_code == 201, f"Неверный статус кода. Ожидался 201, получен {response.status_code}"

# assert response_json["fact"], f"Параметр 'fact' нет в ответе"
# assert response_json["length"], f"Параметр 'length' нет в ответе"
# assert response_json["fact"] is not None, f"Параметр 'fact' пустой"
# assert response_json["fact"] != '', f"Параметр 'fact' пустой"

# assert isinstance(response_json["fact"], str), f"Параметр 'fact' неверный тип данных"
# assert type(response_json["length"]) == int, f"Параметр 'length' неверный тип данных"


