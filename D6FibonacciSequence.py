a = int(input())
b = int(input())
n = int(input())
print(a)
print(b)
for i in range(3, n + 1):
    next = a + b
    print(next)
    a = b
    b = next