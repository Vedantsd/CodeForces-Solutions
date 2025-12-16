n = int(input())
str = ""
for i in range(n): 
    if i % 2 == 0: 
        str += "I hate "
    else: 
        str += "I love "
    if i != n-1: str += "that "

print(str + "it")