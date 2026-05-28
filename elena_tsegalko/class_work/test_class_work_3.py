import requests
import pytest
import allure


@allure.feature("Тест с параметризацией")
@allure.story("Тест на ручки api/v1/Activities/")
@pytest.mark.parametrize("data_id, data_title, data_dueDate, data_completed, status_code",[
                             (10, "32482942", "2026-05-12T16:47:04.313Z", True, 200),
                             ("123424", 223535, '', False, 400),
                             ('', '', 223535, None, 400),
                             (" 32482942 ", " 32482942 ", True, True, 400),
                             (None, None, None, None, 400),
                         ])
# @pytest.mark.skip("Пропускаем")
@pytest.xfail
@allure.title("Позитивные и негативные проверки с параметризацией")
@allure.description("Этот тест проверяет работу ручки с параметрами ... ")
@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label(LabelType.LANGUAGE, "python")
@allure.link("https://dev.example.com/", name="Test")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
class TestApiV1Activities():
    def test_api_v1_activities(data_id, data_title, data_dueDate, data_completed, status_code):
        with allure.step("Подготовка тестовых данных"):
            URL = 'https://fakerestapi.azurewebsites.net/api/v1/Activities'


            payload = {
               "id": data_id,
               "title": data_title,
               "dueDate": data_dueDate,
               "completed": data_completed
        }

    with allure.step("Вызов ручки api/v1/Activities/"):
        response = requests.post(url=URL,
                             json=payload)

    with allure.step("Конвертация ответа в Json"):
        response_json = response.json()

    assert response.status_code == 200

    assert response_json['id'] == data_id
    assert response_json['title'] == data_title
    assert response_json['dueDate'] == data_dueDate
    assert response_json['completed'] == data_completed


# assert response_json["id"] == 0, f"Параметр 'id' не равен 0"
# assert response_json["title"] is not None, f"Параметр 'title' пустой"
# assert type(response_json["completed"]) is bool, f"Тип параметра 'completed' не булевый"