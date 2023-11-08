with open('q2.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
