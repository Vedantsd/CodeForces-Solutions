n = int(input())
for _ in range(n): 
    s = input()
    l = len(s) // 2
    if s[0:l] == s[l:] : 
        print("YES")
    else : 
        print("NO")