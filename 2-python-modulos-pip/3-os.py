import os

# 1 - Consultar funcionalidades do modulo os
# help('os')

# 2 - Retornar a pasta atual
print(os.getcwd())

# 3 - Listar arquivos e pastas
print(os.listdir())

# 4 - Apresentar a versão do sistema operacional
platform = os.uname()
print(platform.sysname)

# 5 - Limpar a tela
os.system('clear')
