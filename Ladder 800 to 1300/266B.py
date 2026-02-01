n, t = map(int, input().split())
s = input()
li = list(s)

for i in range(t):
    j = 0
    while j < (n - 1):
        if li[j] == 'B' and li[j + 1] == 'G':
            li[j], li[j + 1] = li[j + 1], li[j]
            j += 2
        else : 
            j += 1

print(''.join(li)) 