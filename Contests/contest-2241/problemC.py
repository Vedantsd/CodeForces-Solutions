t = int(input())
for _ in range(t): 
    n = int(input())
    s = input()
    transitions = 0
    for i in range(1, n) : 
        if s[i] != s[i - 1] : 
            transitions += 1
    
    print(2 if transitions == 1 else 1)
