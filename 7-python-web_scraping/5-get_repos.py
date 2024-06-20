import requests

# 1 - Mapeando informações
headers = {'X-GitHub-Api-Version': '2022-11-28'}

base_api = 'https://api.github.com'
user = 'OneBitCodeBlog'
url = f'{base_api}/users/{user}/repos'

# 2 - Realizando uma requisição
response = requests.get(url, headers=headers)
print(response.status_code)
print(len(response.json()))
print(response.json())