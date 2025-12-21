t = int(input())
cnt1 = 0
cnt2 = 0

for i in range(t): 
    a, b = map(int, input().split())
    if a > b : cnt1 += 1
    elif a < b : cnt2 += 1
    else : pass

if (cnt1 == cnt2) : print("Friendship is magic!^^")
elif (cnt1 > cnt2) : print("Mishka")
else : print("Chris")