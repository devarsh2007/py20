upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol = ['!', '"', '#', '$', '%', '&', "'" , '(', ')', '*', '+', ',', '-',  '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',  '_', '`', '{', '|', '}', '~']
name = "devarsh"
from random import *
# find pass word from given length
length = int(input("enter length : "))
a = int(length/4)
if length>=4:
    pass1 = choices(upper,k=a)
    pass2 = choices(lower,k=a)
    pass3 = choices(number,k=a)
    pass4 = choices(symbol,k=a)
    password = pass1+pass2+pass3+pass4
    print(password)

    shuffle(password)
    print(password)
    print((("".join(password))))
    
else:
    print("minimum required is 4")