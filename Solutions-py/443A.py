s = input()
s = s.replace("{", "")
s = s.replace("}", "")
S = set(s.split(", "))
S.remove("") if "" in S else None
print(len(S))