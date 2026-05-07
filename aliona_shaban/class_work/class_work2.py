import requests

# URL = 'https://catfact.ninja/fact?max_length=100'
#
# params = {'max_length': 100}
# response = requests.get(url=URL,
#                         params=params)
#
# print(response.status_code)
# response_json = response.json()
# assert response.status_code == 200, f'неверный статус код. Ожидался 200, получен {response.status_code}'
# assert response_json['fact'], f'Параметра "fact" нет в ответе'
# assert response_json['length'], f'Параметра "length" нет в ответе'
#
# assert response_json['fact'] is not None, f'Не пустое'
# assert response_json['length'] > 0, f'Не пустое'
#
# assert isinstance(response_json['fact'], str), f'Не верный тип данных'
# assert type(response_json['length']) == int, f'Не верный тип данных'

URL = 'https://catfact.ninja/facts?max_length=150&limit=20'

params = {'max_length': 150, 'limit': 20}
response = requests.get(url=URL, params=params)

response_json = response.json()
print(response.status_code)

assert response.status_code == 200, f'неверный статус код. Ожидался 200, получен {response.status_code}'

assert response_json['data'][0]['fact'], f'Параметра "fact" нет в ответе'
assert response_json['data'][0]['length'], f'Параметра "length" нет в ответе'

assert response_json['data'][0]['fact'] is not None, f'Не пустое'
assert response_json['data'][0]['length'] > 0, f'Не пустое'

assert isinstance(response_json['data'][0]['fact'], str), f'Не верный тип данных'
assert type(response_json['data'][0]['length']) == int, f'Не верный тип данных'

assert response_json['next_page_url'], f'Параметра "next_page_url" нет в ответе'
assert response_json['path'], f'Параметра "path" нет в ответе'
assert response_json['per_page'], f'Параметра "per_page" нет в ответе'
assert response_json['prev_page_url'], f'Параметра "prev_page_url" нет в ответе'
assert response_json['to'], f'Параметра "to" нет в ответе'
assert response_json['total'], f'Параметра "total" нет в ответе'



