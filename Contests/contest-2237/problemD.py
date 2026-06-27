t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    pref = 0
    cnt = [1, 0, 0]

    bad = 0

    for ch in s:
        if ch == '0':
            pref += 1
        else:
            pref -= 1

        r = pref % 3
        bad += cnt[r]
        cnt[r] += 1

    total = n * (n + 1) // 2
    ans = total - bad

    extra = 0

    i = 0
    while i < n:
        j = i

        while j + 1 < n and s[j] != s[j + 1]:
            j += 1

        length = j - i + 1

        if length % 2 == 0:
            m = length // 2
            odd_sub = m * (m + 1)
        else:
            m = length // 2
            odd_sub = (m + 1) * (m + 1)

        extra += odd_sub - length   

        i = j + 1

    print(ans - extra)