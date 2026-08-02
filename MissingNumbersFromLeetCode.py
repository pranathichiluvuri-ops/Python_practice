a = input().split()
b = []
for i in a:
    b.append(int(i))
    n = len(b)
for i in range(n + 1):
    if b.count(i) == 0:
        print(i)