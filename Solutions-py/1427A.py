t = int(input())
for _ in range(t):
    w, h, n = map(int, input().split())

    p = 1
    while w % 2 == 0:
        w //= 2
        p *= 2
    while h % 2 == 0:
        h //= 2
        p *= 2
    print("YES" if p >= n else "NO")