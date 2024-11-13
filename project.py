import mysql.connector as con
import seller

db = con.connect(host='localhost',password='',user='root',database = 'project20')

print("connection established...")

print("welcome to product management")

print("1 for seller view\n2 for customer view")
choise = int(input("enter your choise : "))

if choise==1:
    print("----------------- seller view --------------------")
    
    
elif choise==2:
    print("-------------------- customer view --------------------")
    
else:
    print("invalid input")