t = int(input())
for _ in range(t): 
    n = int(input())
    if n in range(1400) or (n < 0) : print("Division 4")
    elif n in range(1400, 1600) : print("Division 3")
    elif n in range(1600, 1900) : print("Division 2")
    else : print("Division 1")