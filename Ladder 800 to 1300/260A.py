a, b, n = map(int, input().split())

for i in range(10):
    if ((a * 10) + i) % b == 0 : 
        print(str(a) + str(i) + "0" * (n - 1))
        break
else : 
    print(-1)
