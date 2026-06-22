a = int(input())
for i in range (2, a):
    if a % i == 0:
        print("this is not a prime number")
else:
    print("this is a prime number")