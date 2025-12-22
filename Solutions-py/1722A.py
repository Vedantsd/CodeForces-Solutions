t = int(input())
valid = ['T', 'i', 'm', 'u', 'r']
for i in range(t): 
    n = int(input())
    s = input()
    if n != 5: 
        print("NO")
        continue
    if sorted(s) == sorted("Timur") : 
        print("YES")
    else : 
        print("NO")