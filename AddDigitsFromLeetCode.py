a = int(input())
while a >= 10:
    b = 0
    while a > 0:
        b = b + (a % 10)
        a //= 10
    a = b
print(a)