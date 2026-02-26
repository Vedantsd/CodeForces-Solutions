t = int(input())
for _ in range(t): 
    n = int(input())
    li = list(map(int, input().split()))

    p = li.index(1)

    if p != n - 1: 
        li[p], li[n - 1] = li[n - 1], li[p]
    
    print(*li)