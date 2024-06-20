import requests

# 1 - Dados em um dicionário
new_data = {
    "title": "Aprendendo Python",
    "body": "Manipulando informações de uma API com request",
    "userId": 1,
    "id": 1
}

# 2 - Endpoint da API
url = 'https://jsonplaceholder.typicode.com/posts'

# 3 - Realizando uma requisição POST
post_response = requests.post(
    url, 
    json=new_data
)

print(post_response.status_code)

# 4 - Listar a informação
post_response_json = post_response.json()
print(post_response_json)