import requests

url = "https://api.github.com/search/repositories"
params = {
    "q": "language:html"
}

response = requests.get(url, params=params)

# Печатаем статус-код ответа
print(f"Статус-код: {response.status_code}")

if response.status_code == 200:
    # Если запрос успешен, выводим JSON-данные
    data = response.json()
    print(data)
else:
    print("Ошибка при выполнении запроса:", response.text)