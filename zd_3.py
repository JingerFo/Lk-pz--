import requests

# URL для API
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Отправляем POST-запрос
response = requests.post(url, json=data)

# Печатаем статус-код ответа
print(f"Статус-код: {response.status_code}")

# Печатаем содержимое ответа
if response.status_code == 201:  # 201 Created — успешное создание ресурса
    print("Ответ сервера:")
    print(response.json())
else:
    print("Ошибка при отправке данных!")
    print(response.text)