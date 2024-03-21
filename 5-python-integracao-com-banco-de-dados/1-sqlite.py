import sqlite3

# 1 - Criando uma conexão com o banco de dados
connection = sqlite3.connect('title.db')

# 2 - Verifica se houve alterações na base de dados
print(connection.total_changes)
