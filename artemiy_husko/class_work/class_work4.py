# import requests
# import pytest
# import allure

# @allure.feature('Тест с параметризацией')
# @allure.story('Тест ручки api/v1/Activities')
# @pytest.mark.parametrize('data_id', 'data_title', 'data_due_date', 'data_completed', [
#                                     (0, "string", '2026-05-12T16:46:08.061Z', True, 200),
#                                     ('123423', 54231, '', None, 400),
#                                     ('', '', 54321, None, 400),
#                                     ('56345345', '56345345', True, True, 400),
#                                     (None, None, None, None, 400),
#                                 ])
# @allure.title("Позитивные и негативные тесты")
# def test_api_v1_activities(data_id, data_title, data_due_date, data_completed, status_code):
#     url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

#     payload = {
#         "id": data_id,
#         "title": data_title,
#         "dueDate": data_due_date,
#         "completed": data_completed
#     }
#
# @allure.title("Часть ответа 200 от сервера")
#     response = requests.post(url=url, json=payload)
#     assert response.status_code == status_code
#     data = response.json()
#     assert data["id"] == data_id
#     assert data["title"] == data_title
#     assert data["dueDate"] == data_due_date
#     assert data["completed"] == data_completed


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



import requests
import pytest
import allure


@allure.feature('Тест с параметризацией')
@allure.story('Тест ручки api/v1/Activities')
@allure.description("Этот тест проверяет работу параметров ...")
@allure.tag("API")
@allure.severity("normal")

@allure.label("python")
@allure.label("pytest")
@allure.id("123")
@allure.link("https://github.com/ScoopInstaller/Install#readme")
@allure.issue("TST-123")
@allure.testcase("TEST-1"

@pytest.mark.parametrize('data_id, data_title, data_due_date, data_completed, status_code', [
    (0, "string", '2026-05-12T16:46:08.061Z', True, 200),
    ('123423', 54231, '', None, 400),
    ('', '', 54321, None, 400),
    ('56345345', '56345345', True, True, 400),
    (None, None, None, None, 400),
])

class TestApiV1Activities():
    def test_api_v1_activities(self, data_id, data_title, data_due_date, data_completed, status_code):

        allure.dynamic.title(f"Тест со статус-кодом {status_code}")

        url = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'

        payload = {
            "id": data_id,
            "title": data_title,
            "dueDate": data_due_date,
            "completed": data_completed
        }

        response = requests.post(url=url, json=payload)

        assert response.status_code == status_code
        if status_code == 200:
            data = response.json()
            assert data["id"] == data_id
            assert data["title"] == data_title
            assert data["dueDate"] == data_due_date
            assert data["completed"] == data_completed