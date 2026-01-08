t = int(input())
for _ in range(t): 
    li = list(map(int, input().split()))
    count = 0
    for i in range(1, len(li)): 
        if li[i] > li[0]: count += 1
    
    print(count)