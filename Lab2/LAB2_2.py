
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = {}
matrix2 = {}

print("Enter elements of the first matrix:")
for i in range(rows):
    for j in range(cols):
        value = int(input(f"Enter element at position ({i}, {j}): "))
        if value != 0:
            if i not in matrix1:
                matrix1[i] = {}
            matrix1[i][j] = value

print("Enter elements of the second matrix:")
for i in range(rows):
    for j in range(cols):
        value = int(input(f"Enter element at position ({i}, {j}): "))
        if value != 0:
            if i not in matrix2:
                matrix2[i] = {}
            matrix2[i][j] = value

result_matrix = {}

for i in range(rows):
    if i in matrix1:
        for j in matrix1[i]:
            if i in matrix2 and j in matrix2[i]:
                if i not in result_matrix:
                    result_matrix[i] = {}
                result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

print("Result Matrix:")
for i in range(rows):
    for j in range(cols):
        if i in result_matrix and j in result_matrix[i]:
            print(result_matrix[i][j], end=" ")
        else:
            print(0, end=" ")
    print()
