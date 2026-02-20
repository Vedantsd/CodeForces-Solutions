t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    s = {l, r, d, u}
    print("YES" if len(s) == 1 else "NO")