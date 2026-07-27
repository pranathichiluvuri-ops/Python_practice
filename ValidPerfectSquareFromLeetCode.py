a = int(input())
b = 1
while b * b < a:
    b = b + 1
if b * b == a:
    print("True")
else:
    print("False")