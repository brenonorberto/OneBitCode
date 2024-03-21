import psycopg2

connection = psycopg2.connect(
    database="fliperama",
    user="postgres",
    password="br211201",
    host="localhost",
    port=5432,
)

