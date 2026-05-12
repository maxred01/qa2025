import requests

# URL = 'https://catfact.ninja/fact?max_length=100'
#
# params = {'max_length': 100}
# response = requests.get(url=URL, params=params)
#
# response_json = response.json()
#
# print(response.status_code)
# print(response_json['fact'])
# print(response_json['length'])
#
#
# assert response.status_code == 200, f'Неверный статус код. Ожидался 200. Получили {response.status_code}'
# assert response_json['fact'], f'Параметра "fact" нет в ответе.'
# assert response_json['length'], f'Параметра "length" нет в ответе.'
#
# assert response_json['fact'] is not None, f'Параметр "fact" это пустая строка.'
# assert response_json['length'] != 0, f'Параметр "length" = 0.'
#
# assert isinstance(response_json['fact'], str), f'Неверный тип данных.'
# assert isinstance(response_json['length'], int), f'Неверный тип данных.'

URL_FACTS = 'https://catfact.ninja/facts'
URL_FACT = 'https://catfact.ninja/fact'

params_fact = {'max_length': 100}
response_fact = requests.get(url=URL_FACT, params=params_fact)

params_facts = {'max_length': 10, 'limit': 5}
response_facts = requests.get(url=URL_FACTS, params=params_facts)
links = {'url': 'null' }

response_fact_json = response_fact.json()
response_facts_json = response_facts.json()

assert response_fact.status_code == 200, f'Неверный статус код. Ожидался 200. Получили {response.status_code}'
assert response_fact_json ['fact'], f'Параметра "fact" нет в ответе.'
assert response_fact_json['length'], f'Параметра "length" нет в ответе.'

assert response_fact_json['fact'] is not None, f'Параметр "fact" это пустая строка.'
assert response_fact_json['length'] != 0, f'Параметр "length" = 0.'

assert isinstance(response_fact_json['fact'], str), f'Неверный тип данных.'
assert isinstance(response_fact_json['length'], int), f'Неверный тип данных.'


assert response_facts.status_code == 200, f'Неверный статус код. Ожидался 200. Получили {response.status_code}'
assert response_facts_json['data'][0]['fact'], f'Параметра "fact" нет в ответе.'
assert response_fact_json['data'][0]['length'], f'Параметра "length" нет в ответе.'

assert response_facts_json['data'][0]['fact'] is not None, f'Параметр "fact" это пустая строка.'
assert response_fact_json['data'][0]['length'] != 0, f'Параметр "length" = 0.'

assert isinstance(response_facts_json['data'][0]['fact'], str), f'Неверный тип данных.'
assert isinstance(response_facts_json['data'][0]['length'], int), f'Неверный тип данных.'

assert response_facts_json ['next_page_url'], f'Параметра "next_page_url" нет в ответе.'
assert response_facts_json['length'], f'Параметра "length" нет в ответе.'
