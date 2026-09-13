a = int(input())
count = 0
if a > 1000 or a == 1000:
    count = a - 1000 + 1
    if a > 1000000 or a == 1000000:
        count = 1 + count
    print(count)
else:
    print("0")