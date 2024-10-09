class person:  #perent class
    def walk(self):
        print("i can walk")
        
    def talk(self):
        print("i can talk")
        
class student(person):  #child class
    def read(self):
        print("i can read")
        
    def write(self):
        print("i can write")
        
s1 = student()
s1.walk()
s1.talk()
s1.read()
s1.write()