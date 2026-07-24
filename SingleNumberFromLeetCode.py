a = input()
b = a.split()
for i in b:
    if b.count(i) == 1:
        print(i)