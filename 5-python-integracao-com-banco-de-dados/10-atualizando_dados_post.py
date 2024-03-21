from conexao_post import connection

cursor_obj = connection.cursor()


sql = "UPDATE game SET name = %s WHERE id = %s"

cursor_obj.execute(sql, ("Fifa 23", 5))


connection.commit()
print("Dados atualizados com sucesso!")
connection.close()