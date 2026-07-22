a = int(input())
if a <= 0:
    print("False")
else:
    while a % 2 == 0:
        a = a // 2
    if a == 1:
        print("True")
    else:
        print("False")