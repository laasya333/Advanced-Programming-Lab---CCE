def pascals_triangle(n):
    for line in range(1, n + 1):
        C = 1
        for i in range(1, line + 1):
            print(C, end=" ")  # Print the current coefficient
            C = C * (line - i) // i  # Calculate the next coefficient
        print()  # Move to the next line


n = int(input("Enter the number of rows for Pascal's Triangle: "))
pascals_triangle(n)

