t = int(input())
li = list(map(int, input().split()))
min_val = abs(li[0])

for i in range(1, t):
    min_val = min(min_val, abs(li[i]))

print(min_val)