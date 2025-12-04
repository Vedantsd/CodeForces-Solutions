n = int(input())
count = 0
div = 5
while n > 0:
    count += n // div
    n = n % div
    div -= 1
print(count)