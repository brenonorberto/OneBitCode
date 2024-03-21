import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um BD
'''
cursor = connection.cursor()

# 3 - Solicitando dados do usuário
id = int(input('Qual o ID do filme que deseja atualizar?\n'))
name = input('Qual o novo nome do filme?\n')

# 4 - Atualizando os dados
cursor.execute("""
    UPDATE movies
    SET name = ?
    WHERE id = ?
               """, (name, id))
connection.commit()
print('Filme atualizado com sucesso!')

# 5 - fechando a conexão
connection.close()