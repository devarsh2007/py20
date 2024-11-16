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
    
    sql = "insert into cart(customer_id,product_id,countity) values(%s,%s,%s)"
    mycursor = db.cursor()
    mycursor.execute()
    