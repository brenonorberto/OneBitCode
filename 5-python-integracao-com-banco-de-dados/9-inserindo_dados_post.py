from conexao_post import connection

cursor_obj = connection.cursor()

games = [
    ('Star Wars Survivor', 2023, 9.5),
    ('Luigis Mansion 3', 2019, 9.0),
]

for game in games:
    cursor_obj.execute(
        "INSERT INTO game (name, year, score) VALUES (%s, %s, %s)", game
    )

connection.commit()
print("Dados inseridos com sucesso!")
connection.close()