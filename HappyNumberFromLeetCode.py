a = int(input())
while a != 1: # 1 vachentha varaku ii while loop nadavali
    b = 0
    while a > 0:#a anedhi 0 kanna pedhaga unnatha varuku loop runcheyyu
        b = b + (a % 10) ** 2 # last digit thiyyu, square, and add to b
        a = a // 10# aa loop anedhi next digit ki velladani ki last digit remove cheyyu
        a = b
if a == 1:
    print("True")
else:
    print("False")