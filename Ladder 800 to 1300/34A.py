import math

n = int(input())
li = list(map(int, input().split()))

ans = abs(li[0] - li[1])
x, y = 0, 1

for i in range(1, n - 1):    
    if abs(li[i] - li[i + 1]) < ans : 
        x, y = i, i + 1
    ans = min(ans, abs(li[i] - li[i + 1]))

if abs(li[n - 1] - li[0]) < ans : 
    x, y = n - 1, 0
print(x + 1, y + 1)