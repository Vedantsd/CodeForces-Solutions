lights = []
for _ in range(3): 
    lights.append(list(map(int, input().split())))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

for i in range(3):
    for j in range(3):
        presses = 0
        
        for k in range(5):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < 3 and 0 <= y < 3:
                presses += lights[x][y]
        
        if presses % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()