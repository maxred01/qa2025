# import requests
#
# URL = 'https://catfact.ninja/fact'
#
# params = {'max_length': 100}
# response = requests.get(url=URL,
#                         params=params
#                         )
#
# response_json = response.json()
# assert response.status_code == 200, f"Неверный статус кода. Ожидался 200, получен {response.status_code}"
#
# assert response_json['fact'], f"Параметра 'fact' нет в ответе"
# assert response_json['length'], f"Параметра 'length' нет в ответе"
#
# assert response_json['fact'] is not None, f"Параметр 'fact' пустой"
# assert response_json['length'] is not None, f"Параметр 'length' пустой"
#
# assert isinstance(response_json.get("fact"), str), "Значение 'fact' не является строкой"
# assert isinstance(response_json.get("length"), int), "Значение 'length' не является числом"

import requests

URL = 'https://catfact.ninja/facts'

params = {
    'max_length': 100,
    'limit': 10
}

response = requests.get(url=URL,
                        params=params
                        )

response_json = response.json()
assert response.status_code == 200, f"Неверный статус кода. Ожидался 200, получен {response.status_code}"

assert response_json['data'][0]['fact'], f"Параметра 'fact' нет в ответе"
assert response_json['data'][0]['length'], f"Параметра 'length' нет в ответе"

assert response_json['data'][0]['fact'] is not None, f"Параметр 'fact' пустой"
assert response_json['data'][0]['length'] is not None, f"Параметр 'length' пустой"

assert isinstance(response_json.get("fact"), str), "Значение 'fact' не является строкой"
assert isinstance(response_json.get("length"), int), "Значение 'length' не является числом"

assert response_json['next_page_url'], f"Параметра 'next_page_url' нет в ответе"

