n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort(reverse=True)

pref_sum = [0] * (n + 1)
for i in range(1, n + 1) :
    pref_sum[i] = pref_sum[i-1] + p[i-1] 


for _ in range(q) : 
    x, y = map(int, input().split())

    print(pref_sum[x] - pref_sum[x - y])