import requests

URL_FACTS = 'https://catfact.ninja/facts?max_length=100&limit=3'

params = {
    "max_length": 100,
    "limit": 3
}

response = requests.get(url=URL_FACTS,
                        params=params)

response_json = response.json()

# assert response.status_code == 201, f"Неверный статус код. Ожидался 201, получен {response.status_code}"

# assert response_json["data"]["fact"], f"Параметра 'fact' нет в ответе"
# assert response_json["length"], f"Параметра 'length' нет в ответе"
# assert response_json["fact"] is not None, f"Параметр 'fact' пустой"
# assert response_json["fact"] != '', f"Параметр 'fact' пустой"
#
# assert isinstance(response_json["fact"], str), f"Параметр 'fact' неверный тип данных"
# assert type(response_json["length"]) == int, f"Параметр 'length' неверный тип данных"

assert response_json["next_page_url"], f"Параметра 'next_page_url' нет в ответе"
assert response_json["next_page_url"], f"Параметра 'next_page_url' нет в ответе"

