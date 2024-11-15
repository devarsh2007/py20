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
        Values=[name,id]
        
    elif update == 2:
        desc = input("enter product description : ")
        sql = "update products set description=%s where id=%s"
        Values=[desc,id]
        
    elif update==3:
        price = int(input("enter product price : "))
        sql = "update products set price=%s where id=%s"
        Values=[price,id]
        
    elif update==4:
        isavailable = int(input("enter product status : "))
        sql = "update products set isavailable=%s where id=%s"
        Values=[isavailable,id]
        
    elif update==5:
        name = input("enter product name : ")
        desc = input("enter product description : ")
        price = int(input("enter product price : "))
        isavailable = int(input("enter product status : "))
        sql = "update products set name=%s,description=%s,price=%s,isavailable=%s where id=%s"
        Values=[name,desc,price,isavailable,id]
        
    else:
        print("choise not found")
        
    mycursor = db.cursor()
    mycursor.execute(sql,Values)
    print("data updated successfuly")
    db.commit()
    
    
def select():
    sql = "select * from products"
    mycursor = db.cursor()
    mycursor.execute(sql)
    
    data = mycursor.fetchall()
    # print(data)
    
    # print("id   name    description     price       isavailable")'
    # print("dy",dh)
    # print(f"dy {dh}")

    l1 = ["id","name","description","price","isavailable"]
    print(f"{l1[0]:5} {l1[1]:10} {l1[2]:45}  {l1[3]:10} {l1[4]:10}")
    print("-"*85)

    for i in data:
        print(f"{i[0]:2}    {i[1]:10} {i[2]:40} {i[3]:10} {i[4]:10}")
    