username = input()
s = set()

for ch in username:
    s.add(ch)

if len(s) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
    