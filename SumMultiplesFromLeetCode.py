a = int(input())
total = 0
for i in range(1, a + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        total = total + i
print("Total sum :", total)