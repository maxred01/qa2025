import requests
import validators


URL = 'https://catfact.ninja/breeds?limit=100'
params = {"limit": 100}

response = requests.get(url=URL,
                        params=params)

response_json = response.json()

assert response.status_code == 200, f"Неверный статус код. Ожидался 200, получен {
    response.status_code}"

assert response_json["data"][0]["breed"], "Параметра 'breed' нет в ответе"
assert response_json["data"][0]["country"], "Параметра 'country' нет в ответе"
assert response_json["data"][0]["origin"], "Параметра 'origin' нет в ответе"
assert response_json["data"][0]["coat"], "Параметра 'coat' нет в ответе"
assert response_json["data"][0]["pattern"], "Параметра 'pattern' нет в ответе"

assert response_json["data"][0]["breed"] is not None, "Параметр 'breed' пустой"
assert response_json["data"][0]["country"] is not None, "Параметр 'country' пустой"
assert response_json["data"][0]["origin"] is not None, "Параметр 'origin' пустой"
assert response_json["data"][0]["coat"] is not None, "Параметр 'coat' пустой"
assert response_json["data"][0]["pattern"] is not None, "Параметр 'pattern' пустой"

assert isinstance(response_json["data"][0]["breed"],
                  str), "Параметр 'breed' неверный тип данных"
assert isinstance(response_json["data"][0]["country"],
                  str), "Параметр 'country' неверный тип данных"
assert isinstance(response_json["data"][0]["origin"],
                  str), "Параметр 'origin' неверный тип данных"
assert isinstance(response_json["data"][0]["coat"],
                  str), "Параметр 'coat' неверный тип данных"
assert isinstance(response_json["data"][0]["pattern"],
                  str), "Параметр 'pattern' неверный тип данных"
assert isinstance(response_json["current_page"], int), "Параметр 'current_page' неверный тип данных"
assert isinstance(response_json["from"], int), "Параметр 'from' неверный тип данных"
assert isinstance(response_json["last_page"], int), "Параметр 'last_page' неверный тип данных"
assert isinstance(response_json["per_page"], int), "Параметр 'per_page' неверный тип данных"
assert isinstance(response_json["to"], int), "Параметр 'to' неверный тип данных"
assert isinstance(response_json["total"], int), "Параметр 'total' неверный тип данных"
assert response_json["per_page"] == params.get(
    "limit"), "Параметр 'per_page' не равен значению 'limit'"

assert response_json["first_page_url"], "Параметра 'first_page_url' нет в ответе"
assert validators.url(
    response_json["first_page_url"]), "Не валидный формат 'first_page_url'"
assert response_json["last_page_url"], "Параметра 'last_page_url' нет в ответе"
assert validators.url(
    response_json["last_page_url"]), "Не валидный формат 'last_page_url'"
assert response_json["path"], "Параметра 'path' нет в ответе"
assert validators.url(response_json["path"]), "Не валидный формат 'path'"
assert response_json["next_page_url"] is None, "Параметр 'next_page_url' определён"
assert response_json["prev_page_url"] is None, "Параметр 'prev_page_url' определён"
