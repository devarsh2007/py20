class employee:
    def __init__(self,a,b,c):
        self.name = a  #instance variable
        self.age = b
        self.mobile = c
    
    def display_details(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("mobile : ",self.mobile)
        
        
e1 = employee("devarsh patel",17,1234567890)
e1.display_details()

print("-"*50)
a=input("enter name : ")
b = int(input("enter age : "))
c = int(input("enter mobile no : "))

print("-"*50)
e2 = employee(a,b,c)
e2.display_details()