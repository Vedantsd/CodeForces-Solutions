n, k, l, c, d, p, nl, np = map(int, input().split())

ml = k * l
drink_req = ml // nl

slices = c * d

salt_req = p // np

ans = min(slices, drink_req, salt_req) // n
print(ans)