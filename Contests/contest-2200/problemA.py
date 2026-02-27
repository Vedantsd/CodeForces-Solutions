t = int(input())
for _ in range(t): 
    n = int(input())
    li = list(map(int, input().split()))
    m = max(li)
    print(li.count(m))
