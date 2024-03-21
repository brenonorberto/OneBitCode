from conexao_post import connection

cursor_obj = connection.cursor()


sql = "DELETE FROM game WHERE id = %s"

cursor_obj.execute(sql, (6,))


connection.commit()
print("Dados excluídos com sucesso!")
connection.close()