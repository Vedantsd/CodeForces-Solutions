t = int(input())
for _ in range(t): 
    s = input()

    flag = True

    while len(s) > 1:
        if s[0] == 'Y' and s[1] == 'Y':
            flag = False
            break

        if s[0] != s[1]: 
            s = 'Y' + s[2:]
        else:
            s = 'N' + s[2:]
    
    print("YES" if flag else "NO")