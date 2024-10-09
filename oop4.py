class person:
    salary = 100000
    def __init__(self,name,age,mobile):
        self.name = name
        self.age = age
        self.mobile = mobile
        
    def display(self):
        print(self.name,self.age,self.mobile)
        
p1 = person("devarsh",17,1234512345)

print(person.salary)
p1.salary = 20000
print(p1.salary)