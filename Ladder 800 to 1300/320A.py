s = input()

initOne = s[0] == '1'
threeFours = True
valid = "14"

count = 0
for c in s : 
    if c not in valid : 
        print("NO")
        exit()

    if c == '1' : 
        count = 0
    
    if c == '4' :
        count += 1
        if count > 2 : 
            threeFours = False
            break

if initOne and threeFours :
    print("YES")
else : 
    print("NO")