import requests

URL = 'https://catfact.ninja/fact?max_length=100'

params = {"max_length": 100}
response = requests.get(url=URL,
                        params=params)

response_json = response.json()

# assert response.status_code == 201, f"Неверный статус код. Ожидался 201, получен {response.status_code}"

assert response_json["fact"], f"Параметра 'fact' нет в ответе"
assert response_json["length"], f"Параметра 'length' нет в ответе"
assert response_json["fact"] is not None, f"Параметр 'fact' пустой"
assert response_json["fact"] != '', f"Параметр 'fact' пустой"

assert isinstance(response_json["fact"], str), f"Параметр 'fact' неверный тип данных"
assert type(response_json["length"]) == int, f"Параметр 'length' неверный тип данных"
