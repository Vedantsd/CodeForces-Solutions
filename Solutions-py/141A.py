from collections import Counter

guest = input()
host = input()
pile = input()

combined = guest + host

if Counter(combined) == Counter(pile):
    print("YES")
else:
    print("NO")
