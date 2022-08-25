import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="Ashwin@123")
cursor = mydb.cursor()
cursor.execute("select employee_id,emp_mail from Ashwin1234.ineuron1")
#for i in cursor.fetchall():
#    print(i)

l=[]
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))