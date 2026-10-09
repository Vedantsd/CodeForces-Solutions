n = int(input())
a = []
for i in range(n) : 
    s = input()
    a.append(s)

x = a.count(a[0])

if x > (n // 2) : 
    print(a[0])
else : 
    t = a[0]
    while t in a : 
        a.remove(t)
    print(a[0])