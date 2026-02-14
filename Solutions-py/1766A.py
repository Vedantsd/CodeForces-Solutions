t = int(input())
for _ in range(t):
    n = input().strip()
    length = len(n)
    first = int(n[0])
    ans = 9 * (length - 1) + first
    print(ans)