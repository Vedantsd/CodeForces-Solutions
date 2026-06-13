t = int(input()) 
for _ in range(t) :
    n, k = map(int, input().split())
    s = input()

    flag = True

    for r in range(k):
        o = 0
        for i in range(r, n, k):
            if s[i] == '1':
                o += 1

        if o % 2:
            flag = False
            break

    print("YES" if flag else "NO")