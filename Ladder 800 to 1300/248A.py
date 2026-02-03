t = int(input())
l_count, r_count = 0, 0
for _ in range(t):
    l, r = map(int, input().split())
    l_count += l
    r_count += r

l_min = min(l_count, t - l_count)
r_min = min(r_count, t - r_count)
print(l_min + r_min)