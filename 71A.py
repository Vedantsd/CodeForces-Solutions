words = []

n = int(input())

for i in range (n):
    temp = input()
    words.append(temp)

for i in words:
    if len(i) > 10: 
        print(i[0] + str((len(i) - 2)) + i[-1])
    else: 
        print(i)
