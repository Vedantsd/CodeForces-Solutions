t = int(input())
for _ in range(t): 
    s = set(map(int, input().split()))
    print("YES" if len(s) == 1 else "NO")