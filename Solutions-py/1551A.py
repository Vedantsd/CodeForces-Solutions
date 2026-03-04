t = int(input())
for _ in range(t): 
    n = int(input())

    c = n // 3
    r = n - (c * 3)

    if r == 2: 
        print(c, c + 1)
    else : 
        print((c + r), c)