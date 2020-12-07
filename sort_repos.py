# Этот модуль используется для обработки ответа Api.
# А так же позволяет убедится в том что вызов получил ожидаемую информацию.
import requests

url = 'https://api.github.com/search/repositories?q=q&sort=stars'

r = requests.get(url)
print("Status code", r.status_code) # Статус код 200 - признак успешного ответа.

response_dict = r.json()    # Сохранение  ответа API в переменной.
print(response_dict.keys()) # Обработка результатов.
print("Total repo:", response_dict['total_count']) # Общее кол-во репозиториев.

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print("Repo returned:", len(repo_dicts))

#Анализ первого репозитория.
repo_dict = repo_dicts[0]
print("\bKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# Проанализировав полученную информацию, мы можем вывести её на экран.

# По типу:
# repo_dict = repo_dicts[0]
# print('Name:', repo_dict['name'])
# Либо:
# for repo_dict in repo_dicts:
#    print('\nName:', repo_dict['name'])

# Первый случай используется для обработки информации о определённом репозитории
# Второй для обработки информации о всех репозиториях возвращаемых вызовом API 
