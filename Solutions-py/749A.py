n = int(input())
x = n // 2
print(x)
if n % 2 == 0 : 
    print("2 " * x)
else : 
    print("2 " * (x - 1) + "3")