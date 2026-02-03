n = int(input())
li = list(map(int, input().split()))

count = 0

max_val = li[0]
min_val = li[0]
for i in li:
    if i > max_val or i < min_val: 
        count += 1
        max_val = max(max_val, i)
        min_val = min(min_val, i)

print(count)