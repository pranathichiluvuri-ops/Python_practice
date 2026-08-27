a = int(input())
for i in range(a, 0, -1):
    spaces = " " * (a - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)