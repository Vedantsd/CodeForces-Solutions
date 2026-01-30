n, m = map(int, input().split())

flag = False

for i in range(1, n + 1):
    if i % 2 == 0 : 
        if flag : 
            print('#' + '.' * (m - 1))
            flag = False
        else : 
            print('.' * (m - 1) + '#')
            flag = True
    else : 
        print('#' * m)