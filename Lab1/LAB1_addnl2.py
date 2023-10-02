
num_str = input("Enter a number: ")


digit_sum = 0


num = int(num_str)
num_digits = len(num_str)


temp_num = num
while temp_num > 0:
    digit = temp_num % 10
    digit_sum += digit ** num_digits
    temp_num //= 10


if digit_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

