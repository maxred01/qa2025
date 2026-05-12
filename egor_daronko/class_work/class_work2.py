import requests

url = 'https://catfact.ninja/facts?max_length=100&limit=5'
params = {'max_length': 1000}
response = requests.get(url=url, params=params)
response_json = response.json()


assert response.status_code == 200, f'Неверный статус код. Ожидался 200, получен {response.status_code}'
assert response_json['data'][0]['fact'], f'Параметр "fact" отсутствует в ответе'
assert response_json['data'][0]['length'], f'Параметр "length" отсутствует в ответе'
assert isinstance(response_json['data'][0]["fact"], str), f'Параметр "fact" не типа str, а не {type(response_json["fact"])}'
assert isinstance(response_json['data'][0]["length"], int), f'Параметр "length" не типа int, а не {type(response_json["length"])}'
assert len(response_json['data'][0]["fact"]) > 0, "Поле пустое"
assert len(str(response_json['data'][0]["fact"])) > 0, "Поле пустое"
assert type(response_json['data'][0]["length"]) == int, "Поле пустое или отсутствует"
assert response_json['next_page_url'], f'Параметр "next_page_url" отсутствует в ответе'
assert response_json['path'], f'Параметр "path" отсутствует в ответе'
assert response_json['per_page'], f'Параметр "per_page" отсутствует в ответе'
assert response_json['to'], f'Параметр "to" отсутствует в ответе'
assert response_json['total'], f'Параметр "total" отсутствует в ответе'
