import mysql.connector as con

db = con.connect(host='localhost',user='root',password='',database = 'py20')

print("connection established....")

name = input("enter new name : ")
mobile=int(input("enter new mobile : "))
age = int(input("enter new age : "))
salary = int(input("enter new salary : "))
id=int(input("enter id that you want to change : "))

sql = "update employee set name=%s,mobile=%s,age=%s,salary=%s where id=%s"
values = [name,mobile,age,salary,id]

mycursor = db.cursor()
mycursor.execute(sql,values)
print("row updated successfully....")

db.commit()