n, k = map(int, input().split())

m = (4 * 60) - k 
count = 0
for i in range(1, n + 1): 
    if (5 * i) <= m : 
        count += 1
        m -= (5 * i)
print(count)
