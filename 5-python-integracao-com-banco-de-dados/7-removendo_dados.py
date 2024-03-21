import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um BD
'''
cursor = connection.cursor()

# 3 - Solicitando dados do usuário
id = int(input('Qual o ID do filme que deseja remover?\n'))

# 4 - Removendo dados
cursor.execute("""
    DELETE FROM movies
    WHERE id = ?
               """, (id,))
connection.commit()
print('Filme removido com sucesso!')

# 5 - fechando a conexão
connection.close()