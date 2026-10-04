t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    if n % x != 0:
        print(-1)
        continue

    p = list(range(n + 1))
    p[1] = x

    cur = x

    while cur != n:
        for nxt in range(cur * 2, n + 1, cur):
            if n % nxt == 0:
                p[cur] = nxt
                cur = nxt
                break

    p[n] = 1

    print(*p[1:])