a, b, c = map(int, input().split())
total = a + b + c
diff = (max(a, b, c) - min(a, b, c))
x = total - max(a, b, c) - min(a, b, c)
print("check again" if diff >= 10 else f"final {x}")
