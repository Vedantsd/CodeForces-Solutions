from collections import Counter 

t = int(input())
for _ in range(t): 
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if Counter(a[::2]) == Counter(b[::2]) and Counter(a[1::2]) == Counter(b[1::2]) : 
        print("YES")
    else : 
        print("NO")