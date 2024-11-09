import mysql.connector as con

db = con.connect(host='localhost',user='root',password='',database = 'py20')

print("connection established....")