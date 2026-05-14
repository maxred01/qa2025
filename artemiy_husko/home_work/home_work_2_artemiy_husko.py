import requests

URL = 'https://catfact.ninja/breeds'

params = {'limit': 10}

response = requests.get(url=URL, params=params)

response_json = response.json()
assert response.status_code == 200, f"Неверный статус кода. Ожидался 200, получен {response.status_code}"

assert response_json['data'][0]['breed'], f"Параметра 'breed' нет в ответе"
assert response_json['data'][0]['country'], f"Параметра 'country' нет в ответе"
assert response_json['data'][0]['origin'], f"Параметра 'origin' нет в ответе"
assert response_json['data'][0]['coat'], f"Параметра 'coat' нет в ответе"
assert response_json['data'][0]['pattern'], f"Параметра 'pattern' нет в ответе"

assert response_json['data'][0]['breed'] is not None, f"Параметр 'breed' пустой"
assert response_json['data'][0]['country'] is not None, f"Параметр 'country' пустой"
assert response_json['data'][0]['origin'] is not None, f"Параметр 'origin' пустой"
assert response_json['data'][0]['coat'] is not None, f"Параметр 'coat' пустой"
assert response_json['data'][0]['pattern'] is not None, f"Параметр 'pattern' пустой"

assert isinstance(response_json['data'][0]['breed'], str), "Значение 'breed' не является строкой"
assert isinstance(response_json['data'][0]['country'], str), "Значение 'country' не является строкой"
assert isinstance(response_json['data'][0]['origin'], str), "Значение 'origin' не является строкой"
assert isinstance(response_json['data'][0]['coat'], str), "Значение 'coat' не является строкой"
assert isinstance(response_json['data'][0]['pattern'], str), "Значение 'pattern' не является строкой"

assert response_json['next_page_url'], f"Параметра 'next_page_url' нет в ответе"
assert response_json['path'], f"Параметра 'path' нет в ответе"
assert response_json['per_page'], f"Параметра 'per_page' нет в ответе"
assert response_json['prev_page_url'] is None, f"Параметр 'prev_page_url' есть в ответе"
assert response_json['to'], f"Параметра 'to' нет в ответе"
assert response_json['total'], f"Параметра 'total' нет в ответе"

assert response_json['next_page_url'] is not None, f"Параметр 'next_page_url' пустой"
assert response_json['path'] is not None, f"Параметр path' пустой"
assert response_json['per_page'] is not None, f"Параметр 'per_page' пустой"
assert response_json['to'] is not None, f"Параметр 'to' пустой"
assert response_json['total'] is not None, f"Параметр 'total' пустой"

assert isinstance(response_json['next_page_url'], str), f"Значение 'next_page_url' не является строкой"
assert isinstance(response_json['path'], str), f"Значение 'path' не является строкой"
assert isinstance(response_json['per_page'], int), f"Значение 'per_page' не является числом"
assert isinstance(response_json['to'], int), f"Значение 'to' не является числом"
assert isinstance(response_json['total'], int), f"Значение 'total' не является числом"

assert response_json['links'][1]['url'], f"Параметра 'url' нет в ответе"
assert response_json['links'][1]['label'], f"Параметра 'label' нет в ответе"
assert response_json['links'][1]['active'], f"Параметра 'active' нет в ответе"

assert response_json['links'][1]['url'] is not None, f"Параметр 'url' пустой"
assert response_json['links'][1]['label'] is not None, f"Параметр 'label' пустой"
assert response_json['links'][1]['active'] is not None, f"Параметр 'active' пустой"

assert isinstance(response_json['links'][1]['url'], str), f"Значение 'url' не является строкой"
assert isinstance(response_json['links'][1]['label'], str), f"Значение 'label' не является строкой"
assert isinstance(response_json['links'][1]['active'], bool), f"Значение 'active' не является булевым типом"