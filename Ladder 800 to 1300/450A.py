from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

q = deque((i, a[i]) for i in range(n))
last = 0

while q:
    i, need = q.popleft()
    need -= m
    if need > 0:
        q.append((i, need))
    else:
        last = i + 1

print(last)