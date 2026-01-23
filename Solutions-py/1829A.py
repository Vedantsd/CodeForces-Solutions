t = int(input())
for _ in range(t): 
    s = input()
    string = "codeforces"
    count = 0
    for i in range(len(s)): 
        if s[i] != string[i]: count += 1
    
    print(count)