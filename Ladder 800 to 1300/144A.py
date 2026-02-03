n = int(input())
li = list(map(int, input().split()))

min_val = min(li)
max_val = max(li)
min_idx, max_idx = 0, 0

for i in range(n): 
    if li[i] == max_val:
        max_idx = i
        break

for i in range(n - 1, -1, -1): 
    if li[i] == min_val:
        min_idx = i
        break 

ans = max_idx + (n - 1 - min_idx)
if max_idx > min_idx:
    ans -= 1

print(ans)