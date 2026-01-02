t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()

    same = True
    for i in range(n):
        if s1[i] == 'R' or s2[i] == 'R':
            if s1[i] != s2[i]:
                same = False
                break

    print("YES" if same else "NO")