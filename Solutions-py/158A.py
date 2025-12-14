n, k = map(int, input().split())
li = list(map(int, input().split()))

count = 0
for i in li:
    if i >= li[k - 1] and i > 0:
        count += 1

print(count)