import requests
from collections import Counter
import pandas

# 1 - Autenticação Github

access_token = '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'
headers = {
    'Authorization': 'Bearer ' + access_token,
    'X-GitHub-Api-Version': '2022-11-28'
}

# 2 - Mapeando informações
base_api = 'https://api.github.com'
user = 'OneBitCodeBlog'
url = f'{base_api}/users/{user}/repos'

# 3 - Organizando os dados
repos_list = []
for page_num in range(1, 3):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url_page, headers=headers)
        repos_list.append(response.json())
    except:
        repos_list.append(None)
     
# 4 - Filtrando Resultados
# print(repos_list[0][2]) # página - repositório
# print(repos_list[0][2]['name']) # página - repositório

# 5 - Pegando apenas o nome do repositório
name_repos = []

for page in repos_list:
    for repo in page:
        # print(repo['name'])
        name_repos.append(repo['name'])

print(len(name_repos))
print(name_repos[:10])

# 6 - Pegando a liguagem de cada repositório
language_repos = []

for page in repos_list:
    for repo in page:
        # print(repo['language'])
        language_repos.append(repo['language'])

print(len(language_repos))
print(language_repos[:10])

# 7 - Contando ocorrencia de cada linguagem
print(Counter(language_repos))

# 8 - Criando um DataFrame
dados_obc = pandas.DataFrame()
dados_obc['repo_name'] = name_repos
dados_obc['repo_lang'] = language_repos
print(dados_obc)

# 9 - Salvando em um arquivo .csv
dados_obc.to_csv('dados_obc.csv')