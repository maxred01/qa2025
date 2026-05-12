import requests

url = 'https://catfact.ninja/breeds?limit=2'
params = {'limit': 2}
response = requests.get(url=url, params=params)
response_json = response.json()


assert response.status_code == 200, f'Неверный статус код. Ожидался 200, получен {response.status_code}'
assert response_json['data'][0]['breed'], f'Параметр "breed" отсутствует в ответе'
assert response_json['data'][0]['country'], f'Параметр "country" отсутствует в ответе'
assert response_json['data'][0]['origin'], f'Параметр "origin" отсутствует в ответе'
assert response_json['data'][0]['coat'], f'Параметр "coat" отсутствует в ответе'
assert response_json['data'][0]['pattern'], f'Параметр "pattern" отсутствует в ответе'

assert isinstance(response_json['data'][0]["breed"], str), f'Параметр "breed" не типа str, а {type(response_json["data"][0]["breed"])}'
assert isinstance(response_json['data'][0]["country"], str), f'Параметр "country" не типа str, а {type(response_json["data"][0]["country"])}'
assert isinstance(response_json['data'][0]["origin"], str), f'Параметр "origin" не типа str, а {type(response_json["data"][0]["origin"])}'
assert isinstance(response_json['data'][0]["coat"], str), f'Параметр "coat" не типа str, а {type(response_json["data"][0]["coat"])}'
assert isinstance(response_json['data'][0]["pattern"], str), f'Параметр "pattern" не типа str, а {type(response_json["data"][0]["pattern"])}'

assert len(str(response_json['data'][0]["breed"])) > 0, "Поле пустое"
assert len(str(response_json['data'][0]["country"])) > 0, "Поле пустое"
assert len(str(response_json['data'][0]["origin"])) > 0, "Поле пустое"
assert len(str(response_json['data'][0]["coat"])) > 0, "Поле пустое"
assert len(str(response_json['data'][0]["pattern"])) > 0, "Поле пустое"

assert response_json['next_page_url'], f'Параметр "next_page_url" отсутствует в ответе'
assert response_json['path'], f'Параметр "path" отсутствует в ответе'
assert response_json['per_page'], f'Параметр "per_page" отсутствует в ответе'
assert response_json['to'], f'Параметр "to" отсутствует в ответе'
assert response_json['total'], f'Параметр "total" отсутствует в ответе'
