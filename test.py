import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="Ashwin@123")
cursor = mydb.cursor()
#cursor.execute("create database Ashwin1234")


#s="create table Ashwin1234.ineuron1(employee_id int(10),emp_name varchar(80),emp_mail varchar(80),emp_salary int(6),emp_attendance int(3))"
#cursor.execute(s)

q2=cursor.execute("select*from Ashwin1234.ineuron1")
print(q2)




