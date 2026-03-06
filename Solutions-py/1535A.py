t = int(input())
for _ in range(t): 
    li = list(map(int, input().split()))

    if ((li[2] > li[0] and li[2] > li[1]) and (li[3] > li[0] and li[3] > li[1])) or ((li[0] > li[2] and li[0] > li[3]) and (li[1] > li[2] and li[1] > li[3])):
        print("NO")
    else : 
        print("YES")