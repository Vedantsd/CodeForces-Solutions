n = int(input())
li = list(map(int, input().split()))

bot, top = 0, n - 1
s1, s2 = 0, 0
i = 0

while bot <= top : 

    if i % 2 == 0: 
        s1 += max(li[top], li[bot])
    else : 
        s2 += max(li[top], li[bot])

    if max(li[top], li[bot]) == li[top] : 
        top -= 1
    else : 
        bot += 1

    i += 1

print(s1, s2)