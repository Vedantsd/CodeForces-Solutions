k, r = map(int, input().split())

if (k % 10) in [0, r] : 
    print(1)
else : 
    count = 1
    
    for i in range(1, 11) : 
        if (i * k) % 10 in [0, r]: 
            print(i)
            break