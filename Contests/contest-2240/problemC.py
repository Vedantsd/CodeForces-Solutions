mod = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        continue

    x = 0
    for i in a:
        x ^= i

    if x == 0:
        print(1)
        continue

    ans = 0
    for i in a:
        if (i ^ x) <= i:
            ans += 1

    print(ans % mod)