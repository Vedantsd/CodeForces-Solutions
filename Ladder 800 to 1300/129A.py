n = int(input())
a = list(map(int, input().split()))
s = sum(a)
count = 0
for i in a : 
    if (s - i) % 2 == 0 : 
        count += 1

print(count)