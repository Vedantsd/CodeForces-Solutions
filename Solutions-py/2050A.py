t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    words = [input().strip() for _ in range(n)]
    
    total = 0
    x = 0
    
    for w in words:
        if total + len(w) <= m:
            total += len(w)
            x += 1
        else:
            break
    
    print(x)