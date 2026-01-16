n = int(input())
s = []
for _ in range(n): 
    m = input()
    s.append(m)

count = 1

for i in range(1, len(s)): 
    if s[i] != s[i - 1]: 
        count += 1

print(count)