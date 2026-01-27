t = int(input())
for _ in range(t): 
    n = int(input())
    li = list(map(int, input().split()))

    flag = True 

    for i in range(len(li) - 1) : 
        if (abs(li[i] - li[i + 1]) not in (5, 7)) : 
            flag = False
    
    print("YES" if flag else "NO")  