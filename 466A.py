n, m, a, b = map(int, input().split())

onlySingle = n * a
onlySpecial = ((n + m - 1) // m) * b

special = n // m
remaining = n % m
mixed = special * b + remaining * a

print(min(onlySingle, onlySpecial, mixed))