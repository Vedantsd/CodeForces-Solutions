li = list(map(int, input().split()))
st = input()
sum = 0
for s in st: 
    sum += li[int(s) - 1]
print(sum)