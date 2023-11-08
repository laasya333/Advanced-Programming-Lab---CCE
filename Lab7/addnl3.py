# Importing the sys module to access command line arguments
import sys

# Checking if the correct number of command line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py <filename> <width>")
else:
    # Getting input filename, output filename, and width from command line arguments
    input_filename = sys.argv[1]
    output_filename = "wrapped.txt"
    width = int(sys.argv[2])

    # Opening the input file and reading its lines
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    # List to store wrapped lines
    wrapped_lines = []

    # Looping through each line and wrapping words based on the specified width
    for line in lines:
        words = line.strip().split()
        wrapped_line = ''
        current_length = 0

        # Wrapping words within the specified width
        for word in words:
            if current_length + len(word) <= width:
                wrapped_line += word + ' '
                current_length += len(word) + 1
            else:
                wrapped_lines.append(wrapped_line.strip())
                wrapped_line = word + ' '
                current_length = len(word) + 1

        # Adding the last wrapped line to the list
        wrapped_lines.append(wrapped_line.strip())

    # Writing wrapped lines to the output file
    with open(output_filename, 'w') as file:
        file.write('\n'.join(wrapped_lines))

    print(f"Lines wrapped successfully and saved to '{output_filename}'.")
