t = int(input())
for _ in range(t):
    k = int(input())
    c = list(map(int, input().split()))

    if max(c) >= 3:
        print("YES")
    else:
        cnt = 0
        for i in c:
            if i >= 2:
                cnt += 1
        print("YES" if cnt >= 2 else "NO")