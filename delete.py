import mysql.connector as con

db = con.connect(host='localhost',user='root',password='',database = 'py20')

print("connection established....")

id = int(input("enter id you want to delete : "))
sql = "delete from employee where id=%s"
values = [id]


mycursor = db.cursor()
mycursor.execute(sql,values)
print("row deleted successfully...")


db.commit()