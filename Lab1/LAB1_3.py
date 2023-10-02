n = int(input("Enter the number of strings: "))

count = 0
odd_strings = []

for i in range(n):
    string = input(f"Enter string {i + 1}: ")

    if len(string) >= 2: #length >= 2
        if string[0] == string[-1]: #first last check
            count = count + 1

    if len(string) % 2 != 0: #odd length check
        odd_strings.append(string)

print(f"Number of strings with same first and last character: {count}")
print("Strings with odd length:")
for s in odd_strings:
    print(s)
