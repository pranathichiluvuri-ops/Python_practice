a = list(map(int, input().split()))
b = int(input())
l = len(a)
count = 0
for i in range(l):
    for j in range(i + 1, l):
        for k in range (j + 1, l):
            if a[i] + a[j] + a[k] == b:
                print("Addends =", a[i], a[j], a[k])
                count = 1 + count
print("No.of sets =", count) 