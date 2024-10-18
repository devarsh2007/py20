class a:
    def fun1(self):
        print("class a")
        
class b:
    def fun1(self):
        print("class b")
        
class c(b,a):
    pass
        
obj = c()

obj.fun1()