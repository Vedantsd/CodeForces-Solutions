t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    blocks = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            blocks += 1

    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(blocks) : 
        pref = [0] * (k + 1)
        pref[0] = dp[0]

        for i in range(1, k + 1) : 
            pref[i] = pref[i - 1] + dp[i]
        
        pref2 = [0] * (k + 1)
        pref2[0] = dp[0]

        for i in range(1, k + 1) :
            pref2[i] = dp[i] + pref[i - 1]
        
        dp = pref2
    
    print(dp[k])