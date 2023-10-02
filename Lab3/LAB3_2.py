def unique_elements(input_list):
    unique_set = set(input_list)

    unique_list = list(unique_set)

    return unique_list

input_list = input("enter list: ").split()
result = unique_elements(input_list)
print("Original list:", input_list)
print("List with unique elements:", result)
