n, m = map(int, input().split())
a = list(map(int, input().split()))

initial = 1 
ans = 0

for i in a : 
    if i == initial : 
        continue 
    
    if i > initial : 
        ans += (i - initial)
    else : 
        ans += ((n - initial) + i)
    initial = i 

print(ans)