n = int(input())
li = list(map(int, input().split()))

ans = -1
count = 1
for i in range(1, n) : 
    if li[i - 1] < li[i] : 
        count += 1
    else : 
        ans = max(ans, count)
        count = 1

ans = max(ans, count)

print(ans)