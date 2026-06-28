l = int(input())
u = int(input())
for num in range(l, u + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)