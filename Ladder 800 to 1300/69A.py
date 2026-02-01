n = int(input())
points = []
for i in range(n):
    coords = list(map(int, input().split()))
    points.append(coords)

n1, n2, n3 = 0, 0, 0
for row in points: 
    n1 += row[0]
    n2 += row[1]
    n3 += row[2]

print("YES" if n1 == n2 == n3 == 0 else "NO")
