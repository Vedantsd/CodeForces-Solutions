import math

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    g = 0
    base = a[0]
    for j in range(1, n):
        g = math.gcd(g, abs(a[i] - base))

    print(g)
