a = list(map(int, input().split()))
b = int(input())
l = len(a)
for i in range(l):
    for j in range(i + 1, l):
        if a[i] + a[j] == b:
            print(a[i], a[j])