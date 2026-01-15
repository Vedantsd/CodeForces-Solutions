import math

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
        
    if n <= 2:
        print(1)
    else:
        print(1 + math.ceil((n - 2) / x))
