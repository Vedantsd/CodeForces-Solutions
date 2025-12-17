n = int(input())
li = list(map(int, input().split()))

for i in range(1, n+1): 
    print(li.index(i) + 1, end=" ")