class person:
    def walk(self):
        print("i can walk")
        
    def talk(self):
        print("i can talk")
        
class student(person):
    def read(self):
        print("i can read")
        
    def write(self):
        print("i can write")
        
class employee(person):
    def work(self):
        print("i can work")
        
        
s1 = student()
e1 = employee()
p1 = person()

p1.walk()
p1.talk()

s1.read()
s1.write()
s1.walk()
s1.talk()

e1.work()
e1.walk()
e1.talk()