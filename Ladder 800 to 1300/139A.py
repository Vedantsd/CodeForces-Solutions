p = int(input())
days = list(map(int, input().split()))

s = sum(days)
p %= s
if p == 0:
    p = s

for i in range(7):
    if p <= days[i]:
        print(i + 1)
        break
    p -= days[i]