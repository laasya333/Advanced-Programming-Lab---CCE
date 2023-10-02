import random

num_items = int(input("Enter the number of items in the dictionary: "))


my_dict = {}
count=0

#part a
while count<num_items:
    key = random.randint(0, 100)
    value = input(f"Enter a value for key {key}: ")
    my_dict[key] = value
    count+=1

# part b
numeric_values = [int(value) for value in my_dict.values() if value.isdigit()]
average_numeric = sum(numeric_values) / len(numeric_values) if numeric_values else 0

# part c
string_values = [value for value in my_dict.values() if isinstance(value, str)]

concatenated_string = ''.join(char for char in ''.join(string_values) if not char.isdigit())

print(f"Average of numeric values: {average_numeric}")
print(f"Concatenated string: {concatenated_string}")

#part d
special_characters = set('!@#$%^&*()_+[]{}|;:",.<>?`~')
special_values = [value for value in string_values if all(char in special_characters or char.isspace() for char in value)]

if special_values:
    print("Values with strings containing only special characters:")
    for value in special_values:
        print(value)
else:
    print("No values with strings containing only special characters found.")
