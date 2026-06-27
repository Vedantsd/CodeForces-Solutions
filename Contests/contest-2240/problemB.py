mod = 998244353
t = int(input())
for _ in range(t):
    n, m, r, c = map(int, input().split())
    exp = (r - 1) * m + (c - 1) * n - (r - 1) * (c - 1)
    print(pow(2, exp, mod))