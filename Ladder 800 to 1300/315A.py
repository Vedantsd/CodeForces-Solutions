n = int(input())
a = []
b = []
for _ in range(n) :
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

count = 0
for i in range(n) : 
    flag = False 
    for j in range(n) : 
        if i != j and a[i] == b[j] : 
            flag = True 
            break
    
    if not flag : 
        count += 1

print(count)