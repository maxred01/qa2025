import requests

URL = 'https://catfact.ninja/fact?max_length=1'
params = {'max_length': 100}
response = requests.get(url=URL,
                        params=params)

response_json = response.json()
assert response.status_code == 200, f'Неверный статус КОЖ. Ожидался 200, получен {response.status_code}'
assert response_json['fact'], f'Параметра "fact" нет ответе'
assert response_json['length'], f'Параметра "length" нет ответе'

assert response_json['fact'] is not None, f'Параметра "fact" пустой'
assert response_json['fact'] != '', f'Параметра "fact" нет в ответе'
assert response_json['fact'] > 0, f'Параметра "length" нет в ответе'
assert response_json['fact'] != 0, f'Параметра "length" нет в ответе'
assert response_json['fact'] is not None, f'Параметра "length" пустой'
assert response_json['fact'] == str, f'Параметра "fact" неверный тип данных'
assert response_json['fact'] == int, f'Параметра "length" неверный тип данных'

