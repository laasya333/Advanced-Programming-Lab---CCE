import re

def starts_ends_with_same_character(s):
    pattern = r'^(.).*\1$'
    if re.match(pattern, s):
        return True
    else:
        return False

input_string = input("Enter a string: ")
result = starts_ends_with_same_character(input_string)

if result:
    print("String starts and ends with the same character")
else:
    print("String does not start and end with the same character")
