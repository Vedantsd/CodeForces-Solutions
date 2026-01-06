n = int(input().strip())
events = list(map(int, input().split()))

available = 0
untreated = 0

for e in events:
    if e == -1:
        if available > 0:
            available -= 1
        else:
            untreated += 1
    else:
        available += e

print(untreated)