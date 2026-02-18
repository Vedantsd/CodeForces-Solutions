t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    freq = [0] * (n + 1)

    for x in li:
        freq[x] += 1

    score = 0
    for f in freq:
        score += f // 2

    print(score)
