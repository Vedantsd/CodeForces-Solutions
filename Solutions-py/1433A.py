t = int(input())
for _ in range(t): 
    x = input()

    d = int(x[0])
    k = len(x)

    ans = (d - 1) * 10 + (k * (k + 1)) // 2
    print(ans)