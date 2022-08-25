import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="Ashwin@123")
cursor = mydb.cursor()
cursor.execute("show databases")
print(cursor.fetchall())


