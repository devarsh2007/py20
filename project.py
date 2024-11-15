import mysql.connector as con
import seller

print("1 for seller view\n2 for customer view")
choise = int(input("enter your choise : "))

if choise==1:
    print("----------------- seller view --------------------")
    exit=0
    while exit==0:
        print("\n1 for add\n2 for remove\n3 for update\n4 for fetch products\n5 for exit")
        ch = int(input("enter your choise : "))
        
        if ch==1:
            seller.add()
            
        elif ch==2:
            seller.remove()
            
        elif ch==3:
            seller.update()
            
        elif ch==4:
            seller.select()
            
        elif ch==5:
            exit=1
            print("exited.....")
            
        else:
            print("choise not found")

elif choise==2:
    print("-------------------- customer view --------------------")
    
else:
    print("invalid input")