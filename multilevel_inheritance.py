class student:
    def read(self):
        print("i can read")
        
    def write(self):
        print("i can write")
        
class employee(student):
    def work(self):
        print("i can work")
        
class person(employee):
    def walk(self):
        print("i can walk")
        
    def talk(self):
        print("i can talk")
        
s1 = student()
e1 = employee()
p1 = person()

s1.read()
s1.write()

e1.read()
e1.write()
e1.work()

p1.work()
p1.walk()
p1.talk()
p1.read()
p1.write()