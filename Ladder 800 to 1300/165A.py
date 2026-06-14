n = int(input())
vert = []
for i in range(n) : 
    li = list(map(int, input().split()))
    vert.append(li)


count = 0
for j in range(n) : 
    x, y = vert[j][0], vert[j][1]
    
    l, r, t, b = False, False, False, False
    for k in range(n) :
        if k == j : 
            continue 
        if vert[k][0] < x and vert[k][1] == y : 
            l = True
        if vert[k][0] > x and vert[k][1] == y : 
            r = True
        if vert[k][0] == x and vert[k][1] > y : 
            t = True
        if vert[k][0] == x and vert[k][1] < y : 
            b = True
    
    if l and r and t and b :
        count += 1

print(count)
        