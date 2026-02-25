n, k = map(int, input().split())
y = list(map(int, input().split()))

eligible = 0
for i in y:
    if i + k <= 5:
        eligible += 1

teams = eligible // 3

print(teams)