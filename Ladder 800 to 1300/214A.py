n, m = map(int, input().split())
count = 0
for i in range(1000) : 
    for j in range(1000) : 
        if ((i * i) + j) == n and (i + (j * j)) == m : 
            count += 1

print(count) 