import requests

URL = 'https://catfact.ninja/breeds?limit=100'
params = {'limit': 100}

response = requests.get(url=URL, params=params)

response_json = response.json()
print(response.status_code)

assert response.status_code == 200, f'неверный статус код. Ожидался 200, получен {response.status_code}'

assert response_json['data'][0]['breed'], f'Параметра "breed" нет в ответе'
assert response_json['data'][0]['country'], f'Параметра "country" нет в ответе'
assert response_json['data'][0]['origin'], f'Параметра "origin" нет в ответе'
assert response_json['data'][0]['coat'], f'Параметра "coat" нет в ответе'
assert response_json['data'][0]['pattern'], f'Параметра "pattern" нет в ответе'

assert response_json['data'][0]['breed'] is not None, f'Не пустое'
assert response_json['data'][0]['country'] is not None, f'Не пустое'
assert response_json['data'][0]['origin'] is not None, f'Не пустое'
assert response_json['data'][0]['coat'] is not None, f'Не пустое'
assert response_json['data'][0]['pattern'] is not None, f'Не пустое'

assert isinstance(response_json['data'][0]['breed'], str), f'Не верный тип данных'
assert isinstance(response_json['data'][0]['country'], str), f'Не верный тип данных'
assert isinstance(response_json['data'][0]['origin'], str), f'Не верный тип данных'
assert isinstance(response_json['data'][0]['coat'], str),f'Не верный тип данных'
assert isinstance(response_json['data'][0]['pattern'], str), f'Не верный тип данных'