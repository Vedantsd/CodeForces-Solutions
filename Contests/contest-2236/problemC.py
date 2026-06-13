from math import inf
import sys

input = sys.stdin.readline

def get_dist(start, x):
    dist = {}

    def dfs(v, cost):
        if cost >= dist.get(v, inf):
            return

        dist[v] = cost

        if v == 0:
            return

        add = (x - v % x) % x
        nxt = (v + add) // x

        dfs(nxt, cost + add + 1)

    dfs(start, 0)
    return dist


t = int(input())

for _ in range(t):
    a, b, x = map(int, input().split())

    da = get_dist(a, x)
    db = get_dist(b, x)

    ans = abs(a - b)

    for va, ca in da.items():
        for vb, cb in db.items():
            ans = min(ans, ca + cb + abs(va - vb))

    print(ans)