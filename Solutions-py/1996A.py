t = int(input())

for _ in range(t):
    n = int(input())
    
    animals = n // 4
    if n % 4 != 0:
        animals += 1
        
    print(animals)