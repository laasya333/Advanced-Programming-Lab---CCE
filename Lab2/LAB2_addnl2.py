
input_list1 = input("Enter the first list: ").split()
input_list2 = input("Enter the second list: ").split()


digit_mapping = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}


list1 = []
list2 = []


for item in input_list1:
    integer_value = 0
    for char in item:
        if char in digit_mapping:
            integer_value = integer_value * 10 + digit_mapping[char]
        else:
            print(f"Skipping invalid input: {item}")
            break
    list1.append(integer_value)

for item in input_list2:
    integer_value = 0
    for char in item:
        if char in digit_mapping:
            integer_value = integer_value * 10 + digit_mapping[char]
        else:
            print(f"Skipping invalid input: {item}")
            break
    list2.append(integer_value)


union_list = []
intersection_list = []
difference_list = []

#union
for item in list1:
    exists_in_union = False
    for u in union_list:
        if item == u:
            exists_in_union = True
            break
    if not exists_in_union:
        union_list = union_list + [item]

for item in list2:
    exists_in_union = False
    for u in union_list:
        if item == u:
            exists_in_union = True
            break
    if not exists_in_union:
        union_list = union_list + [item]

#intersection
for item in list1:
    exists_in_intersection = False
    for i in list2:
        if item == i:
            exists_in_intersection = True
            break
    if exists_in_intersection:
        intersection_list = intersection_list + [item]

#diff
for item in list1:
    exists_in_difference = False
    for i in list2:
        if item == i:
            exists_in_difference = True
            break
    if not exists_in_difference:
        difference_list = difference_list + [item]


print("Union:", union_list)
print("Intersection:", intersection_list)
print("Difference (list1 - list2):", difference_list)
