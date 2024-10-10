class bank_details:
    def __init__(self,name,id,password):
        self.name = name
        self.id = id
        self.__password = password
        
    def display(self):
        print(self.name)
        print(self.id)
        
    def password(self):
        print(self.__password)
        
b1 = bank_details("devarsh",101,"start")
b1.display()


print(b1._bank_details__password)
b1.password()