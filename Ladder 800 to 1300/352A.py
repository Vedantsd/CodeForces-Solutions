n = int(input())
a = list(map(int, input().split()))

if a.count(5) >= 9 and a.count(0) >= 1 :     
    k = a.count(5) % 9
    m = a.count(5) - k
    print("5" * m + "0" * a.count(0))
elif a.count(0) >= 1 : 
    print(0)
else : 
    print(-1)