n = int(input())
li = list(map(int, input().split()))

max_num = max(li)
count = 0
for i in li: 
    count += (max_num - i)
print(count)