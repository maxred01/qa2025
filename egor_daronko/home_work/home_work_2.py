import requests

url = 'https://catfact.ninja/breeds'
params = {'limit': 15}

response = requests.get(url=url, params=params)
response_json = response.json()

# Проверка статус-кода
if response.status_code != 200:
    raise AssertionError (
        f'Неверный статус код.' 
        f'Ожидался 200, получен {response.status_code}'
    )

# Проверки после получения статус-кода 200:
#   1. Проверка параметра "data"
assert 'data' in response_json, 'параметр "data" отсутствует'
assert isinstance(response_json['data'], list), '"data" не является списком'
assert len(response_json['data']) > 0, 'Список "data" пустой'

#   2. Проверка элементов списка "data"
response_data_list = response_json['data'][0] #принятые элементы списка "data"
data_fields = ['breed', 'country', 'origin', 'coat', 'pattern'] #все элементы списка "data"
#   Проверка наличия элементов в списке "data"
for data_field in data_fields:
    assert data_field in response_data_list, f'Параметр {data_field} отсутствует в списке "data"'

#   3. Проверка, что элементы списка "data" не пустые
for data_field in data_fields:
    assert response_data_list[data_field] is not None, f'Поле "{data_field}" = None'
    assert len(response_data_list[data_field].strip()) > 0, f'Поле "{data_field}" пустое'

#   4. Проверка на типы данных
for data_field in data_fields:
    assert isinstance(response_data_list[data_field], str), f'Поле "{data_field}" не строковое'

# Проверка наличия параметров dop_param_fields
dop_param_fields = [
    'next_page_url',
    'path',
    'per_page',
    'prev_page_url',
    'to',
    'total'
]

for dop_param_field in dop_param_fields:
    assert dop_param_field in response_json, (
        f'Праметр {dop_param_field} отсутствует'
    )

# Проверка что, поля dop_params_fields не пустые
for dop_param_field in dop_param_fields:
    assert response_json[dop_param_field] is not None, (
        f'Поле "{dop_param_field}" is None'
    )
    if isinstance(response_json[dop_param_field], str):
        assert len(response_json[dop_param_field].strip()) > 0, (
            f'Поле "{dop_param_field}" пустое'
        )

# Проверка типов данных dop_param_fields
for dop_param_field in dop_param_fields:
    assert isinstance(response_json[dop_param_field], (str, int)),  (
        f'Параметр "{dop_param_field}" не str и не int типа'
    )

# Проверка json в response of headers
assert 'application/json' in response.headers['Content-Type']