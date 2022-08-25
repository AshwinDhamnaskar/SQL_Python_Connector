import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="Ashwin@123")
cursor = mydb.cursor()
s = "insert into Ashwin1234.ineuron1 values(101,'Ashwin','ashwin@gmail.com',100,30)"
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
mydb.commit()
cursor.execute("select *from Ashwin1234.ineuron1")
for i in cursor.fetchall():
    print(i)








