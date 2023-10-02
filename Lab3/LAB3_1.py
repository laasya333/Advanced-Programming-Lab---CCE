def mult(numbers):
    result = 1

    for num in numbers:
        result *= num

    return result


inp = input("Enter a list of numbers")
numbers = [float(x) for x in inp.split()]

product = mult(numbers)
print(f"The product of the numbers is: {product}")

