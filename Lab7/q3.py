with open('q1.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print("Lines in Reverse Order:")
for line in reversed(lines):
    print(line.strip())
