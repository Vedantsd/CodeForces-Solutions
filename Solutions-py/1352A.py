t = int(input())
for _ in range(t): 
    n = int(input())
    count = 0
    s = str(n)
    for i in s: 
        if i != '0': 
            count += 1
    
    print(count)

    for i in range(0, len(s)): 
        if s[i] == '0': 
            continue
        print(s[i] + ('0' * (len(s) - i - 1)), end = " ")