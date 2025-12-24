t = int(input())

for _ in range(t):
    k = int(input())
    count = 0
    x = 1

    while True:
        if x % 3 != 0 and x % 10 != 3:
            count += 1
            if count == k:
                print(x)
                break
        x += 1
