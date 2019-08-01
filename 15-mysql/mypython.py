import mysql.connector as mysql

db = mysql.connect(
	host="localhost",
	user="root",
	password="root",
	database="users"
)

conn = db.cursor()

conn.execute("select * from person")

result = conn.fetchall()

print(result)