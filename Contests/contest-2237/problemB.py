from bisect import bisect_left
import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l = [0] * n
    ok = True

    for i in range(n):
        pos = bisect_left(b, a[i])

        if pos == n:
            ok = False
            break

        l[i] = pos + 1

    if not ok:
        print(-1)
        continue

    release = [[] for _ in range(n + 2)]

    for i in range(n):
        release[l[i]].append(i + 1)

    heap = []
    p = []

    for j in range(1, n + 1):
        for x in release[j]:
            heapq.heappush(heap, x)

        if not heap:
            ok = False
            break

        p.append(heapq.heappop(heap))

    if not ok:
        print(-1)
        continue

    bit = [0] * (n + 2)

    def update(idx):
        while idx <= n:
            bit[idx] += 1
            idx += idx & -idx

    def query(idx):
        s = 0

        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx

        return s

    ans = 0
    seen = 0

    for x in p:
        ans += seen - query(x)
        update(x)
        seen += 1

    print(ans)