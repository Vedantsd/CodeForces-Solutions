li = list(map(int, input().split()))
count = 0
li.sort()
for i in range(1, len(li)) : 
    if (li[i] == li[i - 1]) : 
        count += 1
print(count)