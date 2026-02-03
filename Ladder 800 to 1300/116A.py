n = int(input())

ans = 0
curr = 0

for _ in range(n): 
    a, b = map(int, input().split())
    curr = curr + b - a
    ans = max(ans, curr)

print(ans)