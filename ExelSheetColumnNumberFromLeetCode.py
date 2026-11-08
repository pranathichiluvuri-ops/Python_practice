a = input()
b = 0                   
for char in a:
    c = ord(char) - ord('A') + 1 
    b = b * 26 + c 
print(b)