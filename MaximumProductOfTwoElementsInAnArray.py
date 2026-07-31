a = input().split()
b = []
for i in a:
    b.append(int(i))
first = max(b)
b.remove(first)
second = max(b)
print(first * second)