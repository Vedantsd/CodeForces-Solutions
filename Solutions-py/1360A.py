t = int(input())
for _ in range(t):         
    a, b = map(int, input().split())

    s = min(max(2*a, b), max(2*b, a))
    print(s * s)