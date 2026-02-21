t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    cyc = 0
    for i in range(n):
        if (s[i] != s[(i + 1) % n]): 
            cyc += 1
    
    if cyc == 0 : print(1)
    elif cyc == n : print(n)
    else : print(cyc + 1)