
string = input("Enter a string: ")

#set of valid hexadecimal digits
valid = set("0123456789ABCDEF")

if all(char in valid for char in string):
    print(f"{string} is a hexadecimal number.")
else:
    print(f"{string} is not a hexadecimal number.")
