n = int(input())
a = list(map(int, input().split())) 
m = int(input())
b = list(map(int, input().split()))

d = {}
for i in range(n) : 
    d[a[i]] = i

app1, app2 = 0, 0
for i in b: 
    idx = d[i]
    app1 += idx + 1
    app2 += n - idx

print(app1, app2)