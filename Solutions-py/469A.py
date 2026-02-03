n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = set(a[1:] + b[1:])
try : s.remove(0)  
except KeyError : pass
print("I become the guy." if len(s) == n else "Oh, my keyboard!")