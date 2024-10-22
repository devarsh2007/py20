import random

for i in range(10):
    print(round(random.random(),1))
    
print("-"*100)

print(random.uniform(10,20))
print(random.uniform(10,20))
print(random.uniform(10,20))
print(random.uniform(10,20))
print(random.uniform(10,20))

print(random.randint(10,100))
print(random.randint(10,100))
print(random.randint(10,100))
print(random.randint(10,100))

# print(dir(random))
# start , stop , size
print("-"*100)
print(random.randrange(0,100,10))
print(random.randrange(0,10,2))

print("-"*100)
color = ["red","green","blue","black","yellow","orange"]  
print(random.choice(color))
print(random.choices(color,k=3))

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
random.shuffle(numbers)
print(numbers)

# -------------------- exercise ---------------------------
l1=[1,2,3,4,5]

print(l1)
s=int(input("enter starting number : "))
e=int(input("enter ending number : "))

l1 = list(range(s,e))
# print(l2)
random.shuffle(l1)

print(l1)
# -------------------- exercise ---------------------------

