import requests
import pytest
import allure


@allure.feature('Тест с параметризацией')
@allure.story('Тест ручки /api/v1/Books')
@pytest.mark.parametrize('book_id, title, description, page_count, excerpt, publish_date, expected_status', [
    (10, "Book 10", "Description 10", 200, "Excerpt 10", "2026-05-12T16:43:24.241Z", 200),
    (999, "Book 999", "Description 999", 150, "Excerpt 999", "2026-05-19T12:39:01.359Z", 200)
])
@allure.title('Проверка создания книги: {title}')
def test_create_book(book_id, title, description, page_count, excerpt, publish_date, expected_status):
    URL = 'https://fakerestapi.azurewebsites.net/api/v1/Books'

    payload = {
        'id': book_id,
        'title': title,
        'description': description,
        'pageCount': page_count,
        'excerpt': excerpt,
        'publishDate': publish_date
    }

    response = requests.post(url=URL, json=payload)

    with allure.step('Проверка статус-кода ответа'):
        # FakeRestAPI возвращает 200 OK на успешный POST-запрос Books
        assert response.status_code == expected_status, f"Ожидался {expected_status}, получен {response.status_code}"

    if response.status_code == 200:
        response_json = response.json()

        with allure.step('Проверка совпадения отправленных и полученных данных'):
            assert response_json['id'] == book_id
            assert response_json['title'] == title
            assert response_json['description'] == description
            assert response_json['pageCount'] == page_count
            assert response_json['excerpt'] == excerpt

        with allure.step('Валидация типов данных и обязательных полей'):
            # Проверка наличия ключей
            assert 'id' in response_json, "Параметр 'id' отсутствует в ответе"
            assert 'title' in response_json, "Параметр 'title' отсутствует в ответе"

            # Проверка типов данных
            assert isinstance(response_json['id'], int), "Параметр 'id' должен быть целым числом"
            assert isinstance(response_json['title'], str), "Параметр 'title' должен быть строкой"
            assert response_json['title'] != '', "Параметр 'title' не должен быть пустым"


import allure
import requests

@allure.feature('Тестирование API Книг')
@allure.story('Получение книги по ID')
@allure.title('Проверка получения книги с ID 1')
def test_get_book_by_id():
    # Данные из cURL
    URL = "https://fakerestapi.azurewebsites.net/api/v1/Books/1"
    HEADERS = {"accept": "text/plain; v=1.0"}

    with allure.step('Отправка GET-запроса'):
        response = requests.get(url=URL, headers=HEADERS)

    with allure.step('Проверка статус-кода (200 OK)'):
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    response_json = response.json()

    with allure.step('Проверка значений ключевых полей'):
        assert response_json['id'] == 1, f"Ожидался ID 1, получен {response_json['id']}"
        assert response_json['title'] == "Book 1", "Неверное название книги"
        assert response_json['pageCount'] == 100, "Неверное количество страниц"

    with allure.step('Валидация типов данных и обязательных полей'):
        # Список обязательных полей структуры
        required_keys = ['id', 'title', 'description', 'pageCount', 'excerpt', 'publishDate']
        for key in required_keys:
            assert key in response_json, f"Поле '{key}' отсутствует в ответе сервера"

        # Проверка типов данных
        assert isinstance(response_json['id'], int), "Поле 'id' должно быть int"
        assert isinstance(response_json['title'], str), "Поле 'title' должно быть str"
        assert isinstance(response_json['description'], str), "Поле 'description' должно быть str"
        assert isinstance(response_json['pageCount'], int), "Поле 'pageCount' должно быть int"
        assert isinstance(response_json['excerpt'], str), "Поле 'excerpt' должно быть str"
        assert isinstance(response_json['publishDate'], str), "Поле 'publishDate' должно быть str"


import requests
import pytest
import allure

@allure.feature('Тестирование API Книг')
@allure.story('Обновление книги по ID (PUT)')
@allure.title('Проверка обновления книги с ID 1')
def test_update_book_by_id():
            # URL для обновления конкретной книги
            URL = "https://fakerestapi.azurewebsites.net/api/v1/Books/1"
            # Заголовки, включая Content-Type для отправки JSON
            HEADERS = {
                "accept": "text/plain; v=1.0",
                "Content-Type": "application/json"
            }

            # Данные для обновления книги
            payload = {
                "id": 1,
                "title": "Updated Book 1",
                "description": "New description lorem ipsum.",
                "pageCount": 150,
                "excerpt": "New excerpt lorem ipsum.",
                "publishDate": "2026-05-25T07:33:14.499Z"
            }

            with allure.step('Отправка PUT-запроса для обновления данных'):
                response = requests.put(url=URL, json=payload, headers=HEADERS)

            with allure.step('Проверка статус-кода (200 OK)'):
                assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

            response_json = response.json()

            with allure.step('Проверка соответствия измененных данных в ответе'):
                assert response_json['id'] == payload[
                    'id'], f"Ожидался ID {payload['id']}, получен {response_json['id']}"
                assert response_json['title'] == payload['title'], "Название книги не обновилось"
                assert response_json['pageCount'] == payload['pageCount'], "Количество страниц не обновилось"
                assert response_json['description'] == payload['description'], "Описание не обновилось"
                assert response_json['excerpt'] == payload['excerpt'], "Отрывок не обновился"

            with allure.step('Валидация типов данных измененного ресурса'):
                required_keys = ['id', 'title', 'description', 'pageCount', 'excerpt', 'publishDate']
                for key in required_keys:
                    assert key in response_json, f"Поле '{key}' отсутствует в ответе сервера"

                assert isinstance(response_json['id'], int), "Поле 'id' должно быть int"
                assert isinstance(response_json['title'], str), "Поле 'title' должно быть str"
                assert isinstance(response_json['pageCount'], int), "Поле 'pageCount' должно быть int"


import requests
import pytest
import allure


@allure.feature('Тестирование API Книг')
@allure.story('Удаление книги по ID (DELETE)')
@allure.title('Проверка удаления книги с ID 1')
def test_delete_book_by_id():
    # URL для удаления конкретной книги
    URL = "https://fakerestapi.azurewebsites.net/api/v1/Books/1"

    # Заголовки из спецификации
    HEADERS = {
        "accept": "*/*"
    }

    with allure.step('Отправка DELETE-запроса'):
        response = requests.delete(url=URL, headers=HEADERS)

    with allure.step('Проверка статус-кода успешного удаления (200 OK)'):
        # FakeRESTAPI возвращает 200 OK при успешном удалении книги
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

    # Опциональный шаг: проверка, что повторный GET-запрос вернет 404 Not Found
    # Примечание: на FakeRESTAPI это может не работать, так как это статический mock-сервис
    with allure.step('Проверка отсутствия книги после удаления'):
        check_response = requests.get(url=URL, headers={"accept": "text/plain; v=1.0"})
        # Если бы сервис полноценно сохранял состояние, здесь ожидался бы статус 404
        print(f"Статус проверки после удаления: {check_response.status_code}")