import requests
import pytest
import allure


@allure.feature('Тест с параметризацией')
@allure.story("Тест ручки api/v1/Books/")
@pytest.mark.parametrize('data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code', [
    (100, '4334434', 'gf', 67, 'hello ken', "2026-05-12T16:43:35.873Z", 200),
    (89, '1871863', 645, '', True,  False, 400),
    ('', '', 2342345, True, 'ss', None, 400),
    ('1871863', 0, 9, '3435545', True, True, 400),
    (None, None, None, None, None, None, 400)
])
def test_post_book(data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code):
    with allure.step("Подготовка тестовых данных"):
        URL = "https://fakerestapi.azurewebsites.net/api/v1/Books"

    playlaod = {
        "id": data_id,
        "title": data_title,
        "description": data_description,
        "pageCount": data_pageCount,
        "excerpt": data_excerpt,
        "publishDate": data_publishDate,

    }

    @allure.title("Позитивные и негативные проверки с параметризацией")
    @allure.description("Этот тест проверяют ручку с параметрами data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code")

    with allure.step("Вызов ручки api/v1/Books/"):
        response = requests.post(url=URL,
                             json=playlaod)

    with allure.step("Конвертация ответа в json"):
        response_json = response.json()

    with allure.step("Проверка ответов"):
        assert response.status_code == status_code
        assert response_json['id'] == data_id
        assert response_json['title'] == data_title
        assert response_json['description'] == data_description
        assert response_json['pageCount'] == data_pageCount
        assert response_json['excerpt'] == data_excerpt
        assert response_json['publishDate'] == data_publishDate


@pytest.mark.parametrize('data_id, status_code', [
    (5, 200),
    (89, 200),
    (0, 404)
])
def test_get_book(data_id, status_code):
    with allure.step("Подготовка тестовых данных"):
        url = f"https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}"

    @allure.title("Позитивные и негативные проверки с параметризацией")
    @allure.description(
        "Этот тест проверяют ручку с параметрами data_id, status_code")

    with allure.step("Вызов ручки api/v1/Books/"):
        response = requests.get(url=url)

    if status_code == 200:

        with allure.step("Конвертация ответа в json"):
            response_json = response.json()

        with allure.step("Проверка ответов"):
            assert response_json['title'], f'Параметр "title" отсутствует в ответе'
            assert response_json['description'], f'Параметр "description" отсутствует в ответе'
            assert response_json['pageCount'], f'Параметр "pageCount" отсутствует в ответе'
            assert response_json['excerpt'], f'Параметр "excerpt" отсутствует в ответе'
            assert response_json['publishDate'], f'Параметр "publishDate" отсутствует в ответе'

            assert isinstance(response_json["title"], str), f'Параметр "title" не типа str, а {type(response_json["title"])}'
            assert isinstance(response_json["description"], str), f'Параметр "description" не типа str, а {type(response_json["description"])}'
            assert isinstance(response_json["pageCount"], int), f'Параметр "pageCount" не типа str, а {type(response_json["pageCount"])}'
            assert isinstance(response_json["excerpt"], str), f'Параметр "excerpt" не типа str, а {type(response_json["excerpt"])}'
            assert isinstance(response_json["publishDate"], str), f'Параметр "publishDate" не типа str, а {type(response_json["publishDate"])}'
            assert len(str(response_json["title"])) == 0, "Поле пустое"
            assert len(str(response_json["description"])) == 0, "Поле пустое"
            assert len(str(response_json["pageCount"])) == 0, "Поле пустое"
            assert len(str(response_json["excerpt"])) == 0, "Поле пустое"
            assert len(str(response_json["publishDate"])) == 0, "Поле пустое"


@pytest.mark.parametrize('data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code', [
            (6767, 'hddj', 'string', 607, 'hello', "2026-05-12T16:43:35.873Z", 200),
            (89, '1871863', 645, '', True, False, 400),
            ('', '', 2342345, 'ddddd', 'ss', None, 400),
            ('1871863', 0, 9, '3435545', True, True, 400),
            (None, None, None, None, True, None, 400)
])
def test_put_book(data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code):
    with allure.step("Подготовка тестовых данных"):
        URL = f"https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}"

    playlaod = {
        "id": data_id,
        "title": data_title,
        "description": data_description,
        "pageCount": data_pageCount,
        "excerpt": data_excerpt,
        "publishDate": data_publishDate,
    }

    @allure.title("Позитивные и негативные проверки с параметризацией")
    @allure.description(
        "Этот тест проверяют ручку с параметрами data_id, data_title, data_description, data_pageCount, data_excerpt, data_publishDate, status_code")

    with allure.step("Вызов ручки api/v1/Books/"):
        response = requests.put(url=URL,
                             json=playlaod)

    with allure.step("Конвертация ответа в json"):
        response_json = response.json()

    with allure.step("Проверка ответов"):
        assert response.status_code == status_code
        assert response_json['id'] == data_id
        assert response_json['title'] == data_title
        assert response_json['description'] == data_description
        assert response_json['pageCount'] == data_pageCount
        assert response_json['excerpt'] == data_excerpt
        assert response_json['publishDate'] == data_publishDate


@pytest.mark.parametrize('data_id, status_code', [
    (5, 200),
    (8, 200),
    (-1, 400)
])
def test_delete_book(data_id, status_code):
    with allure.step("Подготовка тестовых данных"):
        url = f"https://fakerestapi.azurewebsites.net/api/v1/Books/{data_id}"

    @allure.title("Позитивные и негативные проверки с параметризацией")
    @allure.description(
        "Этот тест проверяют ручку с параметрами data_id, status_code")

    with allure.step("Вызов ручки api/v1/Books/"):
        response = requests.delete(url=url)

    with allure.step("Проверка ответов"):
        assert response.status_code == status_code
