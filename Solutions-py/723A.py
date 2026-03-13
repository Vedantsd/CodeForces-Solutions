x1, x2, x3 = map(int, input().split())

positions = sorted([x1, x2, x3])
median = positions[1]

distance = abs(x1 - median) + abs(x2 - median) + abs(x3 - median)

print(distance)