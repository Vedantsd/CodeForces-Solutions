x = 0

n = int(input())

for i in range(n):
    stmt = input()
    if '++' in stmt: x += 1
    else: x -= 1

print(x)