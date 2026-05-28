import requests
import pytest
import allure
from allure_commons.types import Severity, LabelType


@allure.feature('Тест с параметризацией')
@allure.story("Тест ручки api/v1/Activities/")
@pytest.mark.parametrize('data_id, data_title, data_dueDate, data_completed, status_code', [
    (100, '4334434', "2026-05-12T16:43:35.873Z", True, 200),
    ('1871863', 645, '', False, 400),
     ('', '', 45675648, None, 400),
    ('1871863', '3435545', True, True, 400),
    (None, None, None, None, 400)
])
# @pytest.mark.skip("Пропускаем")
# @allure.title("Позитивные и негативные проверки с параметризацией")
# @allure.description("Этот тест проверяют ручку с параметрами...")
# @allure.tag("API")
@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType, "python")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
class TestApiV1Activities():
    @pytest.mark.parametrize('data_id, data_title, data_dueDate, data_completed, status_code', [
        (100, '4334434', "2026-05-12T16:43:35.873Z", True, 200),
        ('1871863', 645, '', False, 400),
        ('', '', 45675648, None, 400),
        ('1871863', '3435545', True, True, 400),
        (None, None, None, None, 400)
    ])
    @allure.title("Позитивные и негативные проверки с параметризацией")
    def test_api_v1_activities(data_id, data_title, data_dueDate, data_completed, status_code):
        with allure.step("Подготовка тестовых данных"):
            URL = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

            playlaod = {
                "id": data_id,
                "title": data_title,
                "dueDate": data_dueDate,
                "completed": data_completed
            }
        with allure.step("Вызов ручки api/v1/Activities/"):
            response = requests.post(url=URL,
                                     json=playlaod)
        with allure.step("Конвертация ответа в json"):
            response_json = response.json()

        with allure.step("Проверка ответов"):
            assert response.status_code == status_code
            assert response_json['id'] == data_id
            assert response_json['title'] == data_title
            assert response_json['dueDate'] == data_dueDate
            assert response_json['completed'] == data_completed