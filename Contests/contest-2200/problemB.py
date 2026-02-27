t = int(input())
for _ in range(t): 
    n = int(input())
    li = list(map(int, input().split()))

    non_dec = True

    for i in range(n - 1):
        if li[i] > li[i + 1]: 
            non_dec = False
            break
    
    print(n if non_dec else 1)