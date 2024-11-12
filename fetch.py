import mysql.connector as con

db = con.connect(host='localhost',user='root',password='',database = 'py20')

print("connection established....")
sql = "select * from employee where id=%s"
id = int(input("enter id : "))
values = [id]

mycursor = db.cursor(dictionary = True)
mycursor.execute(sql,values)

# data = mycursor.fetchall()
# print(data)
# for i in data:
#     print(list(i.values()))

data = mycursor.fetchone()
print(data)

    