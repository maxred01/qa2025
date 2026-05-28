# import requests
#
# URL = 'https://catfact.ninja/fact?max_length=100'
#
# params = {"max_length": 100}
# response = requests.get(url=URL, params=params)
# response_json = response.json()
# print(response.status_code)
#
# assert response.status_code == 200, f"Неверный статус код. Ожидался 200, получен {response.status_code}"
#
# assert response_json["fact"], f'Параметра "fact" нет ответе'
#
# assert response_json[f'Параметра "length" нет в ответе']
#
# assert response_json['fact'] is not None, [f'Параметр "length" пустой']
#
# assert response_json['length'] > 0, f'Параметр "length" пустой'
#
# assert response_json['length'] != 0, [f'Параметр "length" пустой']
#
# assert response_json['length'] is not None, [f'Параметр "length" пустой']
#
# assert response_json['fact'] == str, [f'Параметр "length" пустой']
#
# assert response_json['length'] == int, [f'Параметр "length" пустой']
#
# assert isinstance(response_json['fact'], str), [f'Параметр "length" пустой']
#
# assert type(response_json['length']) == int, [f'Параметр "length" пустой']

# import requests
# URL = 'https://catfact.ninja/fact?max_length=100'
#
# params = {"max_length": 3}
# limits = {"limit": 5}
# response = requests.get(url=URL, params=params)
# response_json = response.json()
# print(response.status_code)
# assert response.status_code == 200, f"Неверный статус код. Ожидался 200, получен {response.status_code}"
# assert response_json["fact"], f'Параметра "fact" нет ответе'
# assert response_json[f'Параметра "limit" нет в ответе']
# assert response_json['fact'] is not None, [f'Параметр "limit" пустой']
# assert response_json['limit'] > 0, f'Параметр "limit" пустой'
# assert response_json['limit'] != 0, [f'Параметр "limit" пустой']
# assert response_json['limit'] is not None, [f'Параметр "limit" пустой']
# assert response_json['fact'] == str, [f'Параметр "limit" пустой']
# assert response_json['limit'] == int, [f'Параметр "limit" пустой']
# assert isinstance(response_json['fact'], str), [f'Параметр "length" пустой']
# assert type(response_json['length']) == int, [f'Параметр "length" пустой']
# assert response_json["next_page_url"], f'Параметра "next_page_url" нет ответе'
# assert response_json["path"], f'Параметра "path" нет ответе'
# assert response_json["per_page"], f'Параметра "per_page" нет ответе'
# assert response_json["prev_page_url"], f'Параметра "prev_page_url" нет ответе'
# assert response_json["to"], f'Параметра "to" нет ответе'
# assert response_json["total"], f'Параметра "total" нет ответе'
