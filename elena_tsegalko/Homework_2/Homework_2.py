import requests
import validators


URL = 'https://catfact.ninja/breeds?limit=100'
params = {"limit": 100}

response = requests.get(url=URL,
                        params=params)

response_json = response.json()

assert response.status_code == 200, f"Неверный статус код. Ожидался 200, получен {response.status_code}"

assert response_json["data"][0]["breed"], f"Параметра 'breed' нет в ответе"
assert response_json["data"][0]["country"], f"Параметра 'country' нет в ответе"
assert response_json["data"][0]["origin"], f"Параметра 'origin' нет в ответе"
assert response_json["data"][0]["coat"], f"Параметра 'coat' нет в ответе"
assert response_json["data"][0]["pattern"], f"Параметра 'pattern' нет в ответе"

assert response_json["data"][0]["breed"] is not None, f"Параметр 'breed' пустой"
assert response_json["data"][0]["country"] is not None, f"Параметр 'country' пустой"
assert response_json["data"][0]["origin"] is not None, f"Параметр 'origin' пустой"
assert response_json["data"][0]["coat"] is not None, f"Параметр 'coat' пустой"
assert response_json["data"][0]["pattern"] is not None, f"Параметр 'pattern' пустой"

assert isinstance(response_json["data"][0]["breed"], str), f"Параметр 'breed' неверный тип данных"
assert isinstance(response_json["data"][0]["country"], str), f"Параметр 'country' неверный тип данных"
assert isinstance(response_json["data"][0]["origin"], str), f"Параметр 'origin' неверный тип данных"
assert isinstance(response_json["data"][0]["coat"], str), f"Параметр 'coat' неверный тип данных"
assert isinstance(response_json["data"][0]["pattern"], str), f"Параметр 'pattern' неверный тип данных"
assert type(response_json["current_page"]) == int, f"Параметр 'current_page' неверный тип данных"
assert type(response_json["from"]) == int, f"Параметр 'from' неверный тип данных"
assert type(response_json["last_page"]) == int, f"Параметр 'last_page' неверный тип данных"
assert type(response_json["per_page"]) == int, f"Параметр 'per_page' неверный тип данных"
assert type(response_json["to"]) == int, f"Параметр 'to' неверный тип данных"
assert type(response_json["total"]) == int, f"Параметр 'total' неверный тип данных"
assert response_json["per_page"] == params.get("limit"), f"Параметр 'per_page' не равен значению 'limit'"

assert response_json["first_page_url"], f"Параметра 'first_page_url' нет в ответе"
assert validators.url(response_json["first_page_url"]), f"Не валидный формат 'first_page_url'"
assert response_json["last_page_url"], f"Параметра 'last_page_url' нет в ответе"
assert validators.url(response_json["last_page_url"]), f"Не валидный формат 'last_page_url'"
assert response_json["path"], f"Параметра 'path' нет в ответе"
assert validators.url(response_json["path"]), f"Не валидный формат 'path'"
assert response_json["next_page_url"] is None, f"Параметр 'next_page_url' определён"
assert response_json["prev_page_url"] is None, f"Параметр 'prev_page_url' определён"