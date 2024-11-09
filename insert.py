import mysql.connector as con

db = con.connect(host='localhost',user='root',password='',database='py20')
print("connection established....")

name = input("enter your name : ")
mobile=int(input("enter your mobile : "))
age = int(input("enter your age : "))
salary = int(input("enter your salary : "))

sql = "insert into employee(name,mobile,age,salary) values(%s,%s,%s,%s)"
values = [name,mobile,age,salary]

mycursor = db.cursor()

mycursor.execute(sql,values)
print("row inserted successfuly....")

db.commit()