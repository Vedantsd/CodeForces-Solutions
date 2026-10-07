t = int(input())
for _ in range(t) :
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n - 1) : 
        a.sort()
        if a[i] == 2048 : 
            print("YES")
            break
        if a[i] == a[i + 1] : 
            a[i + 1] *= 2
            a[i] = 0
    else :
        print("YES" if a[n - 1] == 2048 else "NO")