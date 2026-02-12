t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    a = li.count(-1) % 2
    b = li.count(0)
    print((a * 2) + b)