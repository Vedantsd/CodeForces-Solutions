t = int(input())
for _ in range(t): 
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    ext = a * 3
    pref = [0]
    for x in ext:
        pref.append(pref[-1] + x)

    ans = 0
    for j in range(n):
        c = j + n         

        left = pref[c] - pref[c - d]
        right = pref[c + d + 1] - pref[c + 1]

        s = left + right
        val = 2 * d * a[j] - s
        if val > 0:
            ans += val

    print(ans)