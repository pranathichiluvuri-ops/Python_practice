n = int(input())
temp = n
reverse = 0 
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
    if reverse == n:
        print("Palindrome")
    else:
        print("Not a Palindrome")
#Original number ni pogottakunda undadaniki temp use chestham.
