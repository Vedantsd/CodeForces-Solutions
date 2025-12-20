n, k = map(int, input().split())

while k > 0:
    digit = n % 10
    if digit != 0:
        n -= 1
    else:
        n //= 10
    
    k -= 1

print(n)