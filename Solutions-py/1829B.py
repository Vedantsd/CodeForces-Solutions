t = int(input())
for _ in range(t): 

    n = int(input())
    li = list(map(int, input().split()))
    
    max_len = 0
    temp = 0
    for j in li: 
        if j == 0:
            temp += 1
        if j == 1: 
            temp = 0
        max_len = max(temp, max_len)
    
    print(max_len)

