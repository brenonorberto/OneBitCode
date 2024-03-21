import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um BD
'''
cursor = connection.cursor()

# 3 - Lendo os dados
data = cursor.execute("""
SELECT * FROM movies
""")
print(data.fetchall())

# 4 - Iterando os dados
for row in cursor.execute('SELECT * FROM movies'):
    print(f'{row}')

# 5 - Ordenando os dados pelo score
print('\nFilmes ordenados pelo score\n')
for row in cursor.execute('SELECT * FROM movies ORDER BY score DESC'):
    print(f'{row}')


# 6 - fechando a conexão
connection.close()