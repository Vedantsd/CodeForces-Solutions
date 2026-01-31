m, n = map(int, input().split())

res = m * (n // 2)
if (n & 1) == 1 : 
    res += m // 2 

print(res)
