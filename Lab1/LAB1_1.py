list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

new_list = []


for num in list1:
    if num % 2 != 0:
        new_list.append(num)

for num in list2:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)




