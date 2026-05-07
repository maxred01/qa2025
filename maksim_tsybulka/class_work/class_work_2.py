import requests

URL_FACT = 'https://catfact.ninja/fact'
URL_FACTS = 'https://catfact.ninja/facts'

params_fact = {'max_length': 100}
response_fact = requests.get(url=URL_FACT,
                             params=params_fact
                             )

params_facts = {
    'max_length': 100,
    'limit': 10,
}
response_facts = requests.get(url=URL_FACTS,
                              params=params_facts
                              )

response_fact_json = response_fact.json()
response_facts_json = response_facts.json()

assert response_fact.status_code == 200, f'Неверный статус код. Ожидался 200, получен {response_fact_json.status_code}'
assert response_fact_json['fact'], f'Параметра "fact" нет в ответе'
assert response_fact_json['length'], f'Параметра "length" нет в ответе'

assert response_fact_json['fact'] is not None, f'Параметра "fact" пустой'
assert response_fact_json['fact'] != '', f'Параметра "fact" пустой'

assert response_fact_json['length'] > 0, f'Параметра "length" пустой'
assert response_fact_json['length'] != 0, f'Параметра "length" пустой'
assert response_fact_json['length'] is not None, f'Параметра "length" пустой'

assert isinstance(response_fact_json['fact'], str), f'Параметра "fact" неверный тип данных'
assert type(response_fact_json['length']) == int, f'Параметра "length" неверный тип данных'





assert response_facts.status_code == 200, f'Неверный статус код. Ожидался 200, получен {response_facts_json.status_code}'
assert response_facts_json['data'][0]['fact'], f'Параметра "fact" нет в ответе'
assert response_facts_json['data'][0]['length'], f'Параметра "length" нет в ответе'

assert response_facts_json['data'][0]['fact'] is not None, f'Параметра "fact" пустой'
assert response_facts_json['data'][0]['fact'] != '', f'Параметра "fact" пустой'

assert response_facts_json['data'][0]['length'] > 0, f'Параметра "length" пустой'
assert response_facts_json['data'][0]['length'] != 0, f'Параметра "length" пустой'
assert response_facts_json['data'][0]['length'] is not None, f'Параметра "length" пустой'

assert isinstance(response_facts_json['data'][0]['fact'], str), f'Параметра "fact" неверный тип данных'
assert type(response_facts_json['data'][0]['length']) == int, f'Параметра "length" неверный тип данных'
