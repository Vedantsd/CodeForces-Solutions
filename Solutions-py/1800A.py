t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    s = s.lower()

    ok = True
    for ch in s:
        if ch not in "meow":
            ok = False
            break

    if not ok:
        print("NO")
        continue

    groups = []
    for ch in s:
        if not groups or groups[-1] != ch:
            groups.append(ch)

    if groups == ['m', 'e', 'o', 'w']:
        print("YES")
    else:
        print("NO")
