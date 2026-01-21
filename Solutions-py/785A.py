t = int(input())
ans = 0
dic = {
    "Tetrahedron" : 4, 
    "Cube" : 6, 
    "Octahedron" : 8,
    "Dodecahedron" : 12, 
    "Icosahedron" : 20
}
for _ in range(t): 
    s = input()
    ans += dic[s]

print(ans)