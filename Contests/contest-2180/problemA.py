import math

t = int(input())

for _ in range(t): 
    a, b, c = map(int, input().split())  

    g = math.gcd(a, c)
    cycle = a // g

    curr = b
    ans = b

    for _ in range(cycle): 
        ans = max(ans, curr)
        curr = (curr + c) % a   

    print(ans)
