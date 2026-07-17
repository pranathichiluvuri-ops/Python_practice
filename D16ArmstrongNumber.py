a = input()
total = 0
for i in a:
    total = total + int(i) ** len(a)
if total == int(a):
    print(a, "is an Armstrong number")
else:
    print(a, "is not an Armstrong number")