n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

arr = []

for i in range(n) : 
    for j in range(m) : 
        if b[j] % a[i] == 0 :
            arr.append(b[j] // a[i])

print(arr.count(max(arr)))