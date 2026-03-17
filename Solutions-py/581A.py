a, b = map(int, input().split())

different_days = min(a, b)
same_days = abs(a - b) // 2

print(different_days, same_days)