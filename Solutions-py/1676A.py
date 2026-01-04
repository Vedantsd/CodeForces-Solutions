t = int(input())
for _ in range(t): 
    s = input()
    n1 = sum(map(int, s[0:3]))
    n2 = sum(map(int, s[3:6]))
    print("YES" if n1 == n2 else "NO")