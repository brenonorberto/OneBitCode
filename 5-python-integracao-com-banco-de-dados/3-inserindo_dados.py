import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
'''
Cursor é um interador que permite navegar e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Inserindo dados
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('The Matrix', 1999, 8.7)
               """)

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Super Mario Bros', 2023, 10)
               """)

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES ('Avatar', 2023, 9.5)
               """)

# 4 - Gravando e fechando a conexão
connection.commit()
print('Dados inseridos com sucesso!')

connection.close()