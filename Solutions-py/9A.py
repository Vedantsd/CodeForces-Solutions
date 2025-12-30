import math

y, w = map(int, input().split())
m = 7 - max(y, w)
p = 6

g = math.gcd(m, p)
print(f"{m // g}/{p // g}")