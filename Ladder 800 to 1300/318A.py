import math

n, k = map(int, input().split())

m = int(math.ceil(n / 2))
if k <= m : 
    print(2 * k - 1)
else : 
    k -= m
    print(2 * k)
