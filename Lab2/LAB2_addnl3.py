
line=''
with open('sample.txt', 'w') as file:
    while count<8:
        line = input(f"Enter line: ")
        file.write(line + '\n')


line_data = {}
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        line = line.strip()
        total_length = len(line)
        line_data[i] = [line, total_length]


print("Dictionary with line numbers and line data:")
for line_number, data in line_data.items():
    print(f"Line {line_number}: {data[0]}, Length: {data[1]}")


letter_frequencies = {}


for line_data_list in line_data.values():
    line_text = line_data_list[0]

    
    for char in line_text:
        if char.isalpha():
            char = char.lower()  # Convert to lowercase to ignore case

            
            if char in letter_frequencies:
                letter_frequencies[char] += 1
            else:
                letter_frequencies[char] = 1

print("\nDictionary with letter frequencies:")
for char, freq in letter_frequencies.items():
    print(f"'{char}': {freq}")
