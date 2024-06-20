import requests

# 1 - Versão e métodos da biblioteca
# print(requests.__version__)
# print(dir(requests))

# 2 - Realizando uma requisição GET
link = 'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.status_code)
print(requisicao.text)