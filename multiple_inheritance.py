class student:
    def read(self):
        print("i can read")
        
    def write(self):
        print("i can write")
        
class employee:
    def work(self):
        print("i can work")
        
class person(student,employee):
    def walk(self):
        print("i can walk")
        
    def talk(self):
        print("i can talk")
        
obj1 = person()
obj2 = employee()
obj3 = student()

obj1.read()
obj1.write()
obj1.work()
obj1.walk()
obj1.talk()

obj2.work()
obj3.read()
obj3.write()