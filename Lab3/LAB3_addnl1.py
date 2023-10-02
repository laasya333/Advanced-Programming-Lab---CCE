def count_upper_lower_letters(input_string):
    uppercase_count = 0
    lowercase_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


input_string = input("Enter a string: ")

uppercase, lowercase = count_upper_lower_letters(input_string)

print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
