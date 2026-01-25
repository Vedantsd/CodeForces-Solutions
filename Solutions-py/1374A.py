t = int(input())
for _ in range(t): 
    x, y, n = map(int, input().split())

    k = n - (n % x) + y 
    if k > n : 
        k -= x 
    
    print(k)    