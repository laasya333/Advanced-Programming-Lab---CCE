
sentence = input("Enter a sentence: ")

words = sentence.split()

word_counts = {}

for word in words:
    
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("Word Counts: ")
for word, count in word_counts.items():
    print(f"{word}: {count}")
