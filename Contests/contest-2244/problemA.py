import math 

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    cnt = 0
    curr = 0
    for i in s:
        if i == '#' : 
            curr += 1
        
        else : 
            cnt = max(cnt, curr)
            curr = 0

    cnt = max(cnt, curr)
    
    print(int(math.ceil(cnt / 2)))