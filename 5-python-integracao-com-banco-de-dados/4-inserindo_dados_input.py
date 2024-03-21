import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Solicitação de dados
name = input('Qual o nome do filme?\n')
year = int(input('Qual o ano de exibição?\n'))
score = float(input('Qual a avaliação do filme?\n'))

# 4 - Inserindo dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)
               """, (name, year, score))


# 5 - Gravando e fechando a conexão
connection.commit()
print('Dados inseridos com sucesso!')

connection.close()