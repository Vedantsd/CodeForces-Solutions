t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    ans = 0
    rem = n
    bit = 0

    while (1 << bit) <= rem:
        cost = 1 << bit
        take = min(k, rem // cost)
        ans += take
        rem -= take * cost
        bit += 1

    print(ans)