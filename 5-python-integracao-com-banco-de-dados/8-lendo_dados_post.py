from conexao_post import connection

cursor_obj = connection.cursor()

cursor_obj.execute("SELECT * FROM game")

result = cursor_obj.fetchall()

for row in result:
    print(row)