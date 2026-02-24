t = int(input())
for _ in range(t): 
    li = list(map(int, input().split()))
    li.sort()
    print("YES" if (li[-1] + li[-2]) >= 10 else "NO")