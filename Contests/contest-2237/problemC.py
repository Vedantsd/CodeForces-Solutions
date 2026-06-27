t = int(input())

for _ in range(t) : 
    n = int(input())
    a = list(map(int, input().split()))


    curr = a[0]

    for i in range(1, n) : 
        if a[i] < curr : 
            curr += a[i]
        else : 
            curr = a[i]
    
    print(curr)