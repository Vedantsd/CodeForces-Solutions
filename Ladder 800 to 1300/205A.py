n = int(input())
cities = list(map(int, input().split()))

mn = min(cities)
if cities.count(mn) > 1 : 
    print("Still Rozdil")
else : 
    print(cities.index(mn) + 1) 