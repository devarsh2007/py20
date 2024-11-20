import mysql.connector as con
db=con.connect(host='localhost',password='',user='root',database='project20')

def available_products():
    sql = "select * from products"
    mycursor = db.cursor()
    mycursor.execute(sql)
    
    data = mycursor.fetchall()
    # print(data)
    
    # print("id   name    description     price       isavailable")'
    # print("dy",dh)
    # print(f"dy {dh}")

    l1 = ["id","name","description","price"]
    print(f"{l1[0]:5} {l1[1]:10} {l1[2]:45}  {l1[3]:10}")
    print("-"*85)

    for i in data:
        if i[4] == 1:
            print(f"{i[0]:2}    {i[1]:10} {i[2]:40} {i[3]:10}")
            
            
def buy_product():
    customerid = int(input("enter your customer id : "))
    available_products()
    d1={}
    
    while True:
        productid = int(input("enter product id : "))
        quntity = int(input("enter product quntity : "))
    
        d1[productid] = quntity
        
        exit = int(input("1 for exit or 0 for continue : "))
        if exit==1:
            break
        
    # print(d1)
    keys = list(d1.keys())
    mycursor = db.cursor()
    for i in keys:
        sql = "insert into cart(customer_id,product_id,quntity) values(%s,%s,%s)"
        l1 = [customerid,i,d1[i]]
        mycursor.execute(sql,l1)
        print("product added to cart ....")
        
    

def make_payment():
    mycursor = db.cursor()
    sql1 = "select product_id,quntity from cart"
    mycursor.execute(sql1)
    data1=mycursor.fetchall()
    d1={}
    for i in data1:
        d1[i[0]]=i[1]
            
    # print(d1)
    l1=[]
    count=0
    sql2 = " select id,name,price from products where id=%s" 
    for i in d1.keys():  
        values=[i]
        mycursor.execute(sql2,values)
        data2 = mycursor.fetchone()
        data2 = list(data2)
        l1.append(data2)
        l1[count].append(d1[i])  #quntity
        subtotal = l1[count][2]*d1[i]
        l1[count].append(subtotal)
        count+=1
        
    # print(l1)
    l2 = ["product id","name","price","quntity","subtotal"]    
    print(l2)
    for i in l1:
        print(i)
        
    total = 0
    for i in l1:
        total += i[4]
        
    print("total : ",total)
        
    print("-"*50)
    cartid=int(input("enter your cart id : "))
    payment = int(input("enter 1 for make payment : "))
    
    if payment==1:
        sql = "insert into payments values('',%s,%s)"
        values=[cartid,"success"]
        mycursor.execute(sql,values)
        print("payment is success....")

    else:
        print("payment is pending....")
    db.commit()