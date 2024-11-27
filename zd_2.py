import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Параметры для фильтрации
params = {
    "userId": 1
}

# Выполняем GET-запрос с параметрами
response = requests.get(url, params=params)

if response.status_code == 200:
    records = response.json()
    print("Полученные записи:")
    for record in records:
        print(record)
else:
    print(f"Ошибка! Статус-код: {response.status_code}")
    print("Ответ сервера:", response.text)