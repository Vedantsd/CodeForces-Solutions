import math

t = int(input())
for _ in range(t) : 
    n = int(input())
    ans = math.ceil(n / 2) - 1
    print(ans)