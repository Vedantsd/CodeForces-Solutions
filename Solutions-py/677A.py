n, h = map(int, input().split())
li = list(map(int, input().split()))
ans = n

for i in li: 
    if i > h: ans += 1

print(ans)