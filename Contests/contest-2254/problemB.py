t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    runs = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            runs += 1

    ans = runs

    for i in range(1, n - 1):
        t1 = 1 if s[i - 1] != s[i] else 0
        t2 = 1 if s[i] != s[i + 1] else 0
        t3 = 1 if s[i - 1] != s[i + 1] else 0

        new_runs = runs + (t3 - t1 - t2)
        if new_runs < ans:
            ans = new_runs

    print(ans)