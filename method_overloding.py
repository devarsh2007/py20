class opration:
    def __init__(self,a=None,b=None):
        self.a = a
        self.b = b
        
    def multiplication(self):
        if(self.a != None and self.b!=None):
            print(self.a*self.b)
            
        elif(self.a != None and self.b==None):
            print(self.a*self.a)
            
        elif(self.a==None and self.b==None):
            print(0)
            
            

o1 = opration(10,20)
o1.multiplication()
o1 = opration(10)
o1.multiplication()
o1 = opration()
o1.multiplication()

num1 = (input("enter number 1 : "))
num2 = (input("enter number 2 : "))

if(len(num1) > 0 and len(num2)>0 and num1!='' and num2!=''):
    o2=opration(int(num1),int(num2))
    o2.multiplication()        
    
elif((len(num1) > 0 and num1!='') or (len(num2)>0 and  num2!='')):
    o3=opration(int(num1))
    o3.multiplication()
    
else:
    o4 = opration()
    o4.multiplication()