n = int(input())
li = list(map(int, input().split()))

S = sum(li)
ans = 0

for f in range(1, 6):
    if (S + f) % (n + 1) != 1:
        ans += 1

print(ans)
