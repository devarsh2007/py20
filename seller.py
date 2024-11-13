import mysql.connector as con

db = con.connect(host='localhost',password='',user='root',database = 'project20')

print("connection established...")


def add():
    name = input("enter product name : ")
    desc = input("enter product description : ")
    price = int(input("enter product price : "))
    available = int(input("enter 1 for available or 2 for not available : "))
    
    sql = "insert into products(name,description,price,isavailable) values(%s,%s,%s,%s)"
    values = [name,desc,price,available]
    
    
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    print("product insrted successfuly....")
    
    db.commit()
    
def remove():
    id = int(input("enter id, you want to remove : "))
    sql = "delete from products where id=%s"
    values = [id]
    
    
    mycursor = db.cursor()
    mycursor.execute(sql,values)
    print("product deleted successfuly....")
    
    db.commit()
    
def update():
    id = int(input("enter id you want to update : "))
    print("update : 1 for name\n2 for description\n3 for price\n4 for isavailable\n5 for all")
    
    update = int(input("enter your choise : "))
    
    if update==1:
        name = input("enter product name : ")
        sql = "update products set name=%s where id=%s"