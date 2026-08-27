a = int(input())
for i in range(1, a + 1):
    spaces = " " * (a - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)