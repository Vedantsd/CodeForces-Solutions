s = input()
up_cnt, low_cnt = 0, 0

for i in s: 
    if i.isupper(): up_cnt += 1
    else : low_cnt += 1

print(s.upper() if (up_cnt > low_cnt) else s.lower())