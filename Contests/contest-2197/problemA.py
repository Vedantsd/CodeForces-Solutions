def digit_sum(n):
    return sum(int(d) for d in str(n))

t = int(input())
for _ in range(t):
    x = int(input())
    
    cnt = 0
    for y in range(x, x + 82):
        if y - digit_sum(y) == x:
            cnt += 1
    
    print(cnt)
