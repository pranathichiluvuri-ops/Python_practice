a = input()
b = input()
c = 0
for i in a:
    if a.count(i) > b.count(i):
        c = c + 1
if c == 0:
    print("True")
else:
    print("False")