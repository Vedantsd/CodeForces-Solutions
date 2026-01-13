n = int(input())

used = 0
height = 0
i = 1

while True:
    level = i * (i + 1) // 2
    if used + level > n:
        break
    used += level
    height += 1
    i += 1

print(height)
