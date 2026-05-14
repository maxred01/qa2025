import importlib

import requests
import pytest
import allure
from allure_commons.types import Severity, LabelType

@allure.feature('Тест с параметрами')
@allure.story('Тест /api/v1/Books/')
@pytest.mark.parametrize('data_id, data_title, data_description, data_page_count,'
                         'data_excerpt, data_publish_date, status_code', [
                        (0, 'string', 'string', 0, 'string', '2026-05-13T20:55:24.941Z', 200),
                        ('', '', 0, 'string', 0, 'string', 401),
                        (None, None, None, None, None, None, 400),
                        ('123423', 54231, '', False, None, 'xswdwsay', 400),
                        ])
@allure.title('Проверки теста')
@allure.description('Этот проект проверяет ручки ...')
@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label(LabelType.LANGUAGE, 'pyton')
@allure.link('https://fakerestapi.azurewebsites.net/index.html', name='Website')
@allure.issue('AUTH-123')
@allure.testcase('TMS-456')

def test_api_v1_books(data_id, data_title, data_description, data_page_count, data_excerpt,
                      data_publish_date, status_code):
    with allure.step('Подготовка тестовых данных'):
        URL = 'https://fakerestapi.azurewebsites.net/api/v1/Books/'
        payload = {
        "id": data_id,
        "title": data_title,
        "description": data_description,
        "excerpt": data_excerpt,
        "pageCount": data_page_count,
        "publishDate": data_publish_date
        }
    with allure.step('Вызов /api/v1/Books/'):
        response = requests.post(url=URL, json=payload)

    with allure.step('Перевод ответа в json'):
        response_json = response.json()

    with allure.step('Написание тестов'):

        assert response.status_code == 200, f'неверный статус код. Ожидался 200, получен {response.status_code}'

        assert response_json['id'] == data_id, f'Неправильное значение'
        assert response_json['title'] is not None, f'Не пустое поле'
        assert response_json['description'] is not None, f'Не пустое поле'
        assert response_json['excerpt'] is not None, f'Не пустое поле'
        assert isinstance(response_json['pageCount'], int), f'Не верный тип данных'
        assert response_json['publishDate'] is not None, f'Не пустое поле'

        assert response_json['id'] == data_id
        assert response_json['title'] == data_title
        assert response_json['description'] == data_description
        assert response_json['excerpt'] == data_excerpt
        assert response_json['pageCount'] == data_page_count
        assert response_json['publishDate'] == data_publish_date
#
#
# URL = 'https://fakerestapi.azurewebsites.net/api/v1/Books/12562/'
# params = {'books': 12562}
# response = requests.get(url=URL, params=params)
# print(response.status_code)
# response_json = response.json()
#
# assert response.status_code == 404, (f'неверный статус код. Ожидался 404,'
#                                      f' получен {response.status_code}')
# assert response_json['type'], f'Параметра "type" нет в ответе'
# assert response_json['title'], f'Параметра "title" нет в ответе'
# assert response_json['status'], f'Параметра "status" нет в ответе'
# assert response_json['traceId'], f'Параметра "traceId" нет в ответе'
# assert response_json['type'] is not None, f'Не пустое поле'
# assert response_json['title'] is not None, f'Не пустое поле'
# assert response_json['status'] is not None, f'Не пустое поле'
# assert response_json['traceId'] is not None, f'Не пустое поле'
# assert isinstance(response_json['traceId'], str), f'Не верный тип данных'
# assert isinstance(response_json['type'], str), f'Не верный тип данных'
# assert isinstance(response_json['status'], int), f'Не верный тип данных'
# assert isinstance(response_json['title'], str), f'Не верный тип данных'
#
# import requests
# import pytest
#
#
# @pytest.mark.parametrize('data_id, data_title, data_description, data_page_count,'
#                          'data_excerpt, data_publish_date, status_code', [
#                         (0, 'string', 'string', 0, 'string', '2026-05-14T10:41:26.555Z', 200),
#                         ('', '', 0, 'string', 0, 'string', 401),
#                         (None, None, None, None, None, None, 400),
#                         ('123423', 54231, '', False, None, '', 400),
#                         ])
#
# def test_api_v1_books_145555(data_id, data_title, data_description, data_page_count,
#                              data_excerpt, data_publish_date, status_code):
#     URL = 'https://fakerestapi.azurewebsites.net/api/v1/Books/145555/'
#     payload = {
#     "id": data_id,
#     "title": data_title,
#     "description": data_description,
#     "pageCount": data_page_count,
#     "excerpt": data_excerpt,
#     "publishDate": data_publish_date
#     }
#     response = requests.put(url=URL, json=payload)
#     response_json = response.json()
#
#     assert response_json['id'] == data_id
#     assert response_json['title'] == data_title
#     assert response_json['description'] == data_description
#     assert response_json['excerpt'] == data_excerpt
#     assert response_json['pageCount'] == data_page_count
#     assert response_json['publishDate'] == data_publish_date
#
#     assert response.status_code == 200, (f'неверный статус код. Ожидался 200,'
#                                      f'получен {response.status_code}')
#     assert response_json['id'] == data_id, f'Неправильное значение'
#     assert response_json['title'] == data_title, f'Неправильное значение'
#     assert response_json['description'] == data_description, f'Неправильное значение'
#     assert response_json['pageCount'] == data_page_count, f'Неправильное значение'
#     assert response_json['excerpt'] == data_excerpt, f'Неправильное значение'
#     assert response_json['publishDate'] == data_publish_date, f'Неправильное значение'
#
#     assert response_json['id'] is not None, f'Не пустое поле'
#     assert response_json['title'] is not None, f'Не пустое поле'
#     assert response_json['description'] is not None, f'Не пустое поле'
#     assert response_json['pageCount'] is not None, f'Не пустое поле'
#     assert response_json['excerpt'] is not None, f'Не пустое поле'
#     assert response_json['publishDate'] is not None, f'Не пустое поле'
#
#     assert isinstance(response_json['title'], str), f'Не верный тип данных'
#     assert isinstance(response_json['id'], str), f'Не верный тип данных'
#     assert isinstance(response_json['description'], str), f'Не верный тип данных'
#     assert isinstance(response_json['pageCount'], int), f'Не верный тип данных'
#     assert isinstance(response_json['excerpt'], str), f'Не верный тип данных'
#     assert isinstance(response_json['publishDate'], str), f'Не верный тип данных'
#
# URL = 'https://fakerestapi.azurewebsites.net/api/v1/Books/146413'
# params = {'books': 146413}
# response = requests.get(url=URL, params=params)
# print(response.status_code)
# response_json = response.json()
#
# assert response.status_code == 200, (f'неверный статус код. Ожидался 200,'
#                                      f' получен {response.status_code}')
#

