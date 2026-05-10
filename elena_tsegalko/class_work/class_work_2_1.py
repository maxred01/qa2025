import requests
import validators

URL_FACTS = 'https://catfact.ninja/facts?max_length=100&limit=3'

params = {
    "max_length": 100,
    "limit": 3
}

response = requests.get(url=URL_FACTS,
                        params=params)

response_json = response.json()

assert response.status_code == 200, f"Неверный статус код. Ожидался 200, получен {response.status_code}"
assert len(response_json["data"]) == params.get("limit"), f"Колличество facts не равно limit"
assert response_json["data"][0]["fact"], f"Параметра 'fact' нет в ответе"
assert response_json["data"][0]["length"], f"Параметра 'length' нет в ответе"
assert response_json["data"][0]["fact"] is not None, f"Параметр 'fact' пустой"
assert response_json["data"][0]["fact"] != '', f"Параметр 'fact' пустой"

assert isinstance(response_json["data"][0]["fact"], str), f"Параметр 'fact' неверный тип данных"
assert type(response_json["data"][0]["length"]) == int, f"Параметр 'length' неверный тип данных"

assert response_json["next_page_url"], f"Параметра 'next_page_url' нет в ответе"
assert validators.url(response_json["next_page_url"]), f"Не валидный формат 'next_page_url'"
assert response_json["first_page_url"], f"Параметра 'first_page_url' нет в ответе"
assert validators.url(response_json["first_page_url"]), f"Не валидный формат 'first_page_url'"
assert response_json["last_page_url"], f"Параметра 'last_page_url' нет в ответе"
assert validators.url(response_json["last_page_url"]), f"Не валидный формат 'last_page_url'"
assert response_json["path"], f"Параметра 'path' нет в ответе"
assert validators.url(response_json["path"]), f"Не валидный формат 'path'"
assert response_json["prev_page_url"] is None, f"Параметр 'prev_page_url' не равен null"