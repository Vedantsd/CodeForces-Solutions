t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    carry = 0
    prev = 0
    ok = True

    for i in range(n - 1):
        available = a[i] + carry
        need = prev + 1

        if available < need:
            ok = False
            break

        carry = available - need
        prev = need

    if ok and a[-1] + carry > prev:
        print("YES")
    else:
        print("NO")