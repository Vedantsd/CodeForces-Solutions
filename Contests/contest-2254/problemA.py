t = int(input())
for _ in range(t) :
    a, b, c = map(int, input().split())

    if a == b or a == c or b == c : 
        print(0)
    else : 
        mi = min(a, b, c)
        ma = max(a, b, c)
        mid = a + b + c - mi - ma

        print(min(mid - mi, ma - mid))