n = int(input())
s = input()
cnt = 0
for c in s: 
    if c == 'A': cnt += 1
if cnt > (n - cnt): 
    print("Anton")
elif cnt < (n - cnt): 
    print("Danik")
else: 
    print("Friendship")