t = int(input())
for _ in range(t): 
    s = input()
    for i in range(0, len(s) - 1, 2) :
        print(s[i], end='')
    print(s[-1])