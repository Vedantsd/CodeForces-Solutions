t = int(input())

for i in range(t): 
    n = int(input())
    str_array = input().split(' ')
        
    ans = ""
    for x in str_array:
        if (ans + x) < (x + ans):
            ans += x 
        else:
            ans = x + ans

    print(ans)