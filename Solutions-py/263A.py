li = []
for i in range(5):
    tup = list(map(int, input().split()))
    if 1 in tup : 
        row = i
        count = 0
        for t in tup : 
            if t == 1: 
                col = count
            count += 1

    li.append(tup)

print(abs(row - 2) + abs(col - 2))