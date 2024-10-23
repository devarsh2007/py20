upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol = ['!', '"', '#', '$', '%', '&', "'" , '(', ')', '*', '+', ',', '-',  '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',  '_', '`', '{', '|', '}', '~']

from random import *

pass1 = choices(upper,k=4)

pass2 = choices(lower,k=4)
pass3 = choices(number,k=4)
pass4 = choices(symbol,k=4)

password = pass1+pass2+pass3+pass4
print(password)

shuffle(password)
print(password)
print((len("".join(password))))