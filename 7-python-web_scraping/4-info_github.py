import requests

# 1 - Api events do github
url = 'https://api.github.com/events'

response = requests.get(url)
print(response.status_code)
print(response.json())

# 2 - Verificando a versão da api
url2 = 'https://api.github.com/versions'

response2 = requests.get(url2)
print(response2.json())

# 3 - Realizando uma requisição com versão especifica
headers = {'X-GitHub-Api-Version': '2022-11-28'}
response3 = requests.get(url, headers=headers)
print(response3.json())

