t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    seen = set()
    seen.add(s[0])
    
    for i in range(1, n):
        if s[i] != s[i-1]:
            if s[i] in seen:
                print("NO")
                break
            seen.add(s[i])
    else:
        print("YES")