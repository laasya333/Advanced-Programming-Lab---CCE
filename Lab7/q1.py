with open('q1.txt', 'r', encoding='utf-8') as file:
    content = file.read()

total_chars = len(content)

total_words = len(content.split())

total_lines = len(content.splitlines())

print("Total Characters:", total_chars)
print("Total Words:", total_words)
print("Total Lines:", total_lines)
