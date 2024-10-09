class person:
    def __init__(self,id,name,branch):
        self.id = id
        self.name = name
        self.branch = branch
        print(self.id)
        print(self.name)
        print(self.branch)

class employee(person):
    def __init__(self, id, name, branch,salary,leave):
        super().__init__(id, name, branch)
        # person.__init__(id,name,branch)
        self.salary = salary
        self.leave = leave
        
        print(self.salary)
        print(self.leave)
        
e1 = employee(101,"devarsh","it",11111,2)
p1= person(102,"ram","it")