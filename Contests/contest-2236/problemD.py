from collections import Counter

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = Counter(a)
    vals = sorted(freq)

    m = len(vals)
    dp = [False] * m

    for i in range(m - 1, -1, -1):
        if i == m - 1 or vals[i + 1] - vals[i] > k:
            dp[i] = (freq[vals[i]] % 2 == 0)
        else:
            if not dp[i + 1]:
                dp[i] = True
            else:
                dp[i] = (freq[vals[i]] % 2 == 0)

    print("YES" if any(dp) else "NO")