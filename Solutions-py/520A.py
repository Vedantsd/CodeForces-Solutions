n = int(input())
string = input().lower()
s = set()
for i in string: 
    s.add(i)

print("YES" if len(s) == 26 else "NO") 