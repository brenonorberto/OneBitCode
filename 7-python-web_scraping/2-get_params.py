import requests

# 1 - Api jsonplaceholder
url = 'https://jsonplaceholder.typicode.com/posts'

# 2 - Adicioando um payload
payload = {
    "id": [1, 2, 3, 4, 5],
    "userId": 1,
}

# 3 - Realizando uma requisição
response = requests.get(url, params=payload)

# print(response)
# print(response.json())

# 4 - Melhorando a legibilidade
response_json = response.json()
for i in response_json:
    print(i, '\n')