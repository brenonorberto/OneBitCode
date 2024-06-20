import requests

# Api jsonplaceholder
url = 'https://jsonplaceholder.typicode.com/posts/1'

# 2 - Realizando uma requisição GET
response = requests.get(url)

print(response)
print(response.status_code)

# 3 - Exemlo de tratamento
if response.status_code == 200:
    print('Requisição realizada com sucesso!')
else:
    print('Requisição falhou!')
    
# 4 - Pegar o conteudo da requisição
response_json = response.json()
print(response_json)