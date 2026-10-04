t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    pa = []
    pb = []

    for i, c in enumerate(a):
        if c == '1':
            pa.append(i)

    for i, c in enumerate(b):
        if c == '1':
            pb.append(i)

    if len(pa) != len(pb):
        print(-1)
        continue

    ok = True
    ans = 0

    for x, y in zip(pa, pb):
        if (x & 1) != (y & 1):
            ok = False
            break
        ans += abs(x - y) // 2

    print(ans if ok else -1)