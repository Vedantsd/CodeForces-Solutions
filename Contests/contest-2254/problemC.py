t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    if a.count('1') != b.count('1'):
        print("NO")
        continue

    even_a = sum(a[i] == '1' for i in range(0, n, 2))
    even_b = sum(b[i] == '1' for i in range(0, n, 2))

    print("YES" if even_a == even_b else "NO")