n = int(input())
year = n + 1
while True : 
    s = str(year)
    if (len(s) == len(set(s))) : 
        print(year)
        break
    year += 1
