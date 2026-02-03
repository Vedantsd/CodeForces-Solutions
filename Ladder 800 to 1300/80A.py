import math

def is_prime(num) : 
    if num <= 1 : return False
    for i in range(2, int(math.sqrt(num)) + 1) : 
        if (num % i == 0) : 
            return False
    return True

def next_prime(num) : 
    prime = num + 1
    while (not is_prime(prime)) : 
        prime += 1
    return prime

n, m = map(int, input().split())
print("YES" if next_prime(n) == m else "NO")