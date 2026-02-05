
n = int(input())

p = []
v = []
t = []

for i in range(n) :
    x, y, z = map(int, input().split())
    p.append(x)
    v.append(y)
    t.append(z)

count = 0

for i in range(n) :
    tmp = p[i] + v[i] + t[i]
    if tmp >= 2: count += 1

print(count)