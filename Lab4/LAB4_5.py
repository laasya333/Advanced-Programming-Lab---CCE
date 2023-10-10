import string

sentence = input("Enter sentence: ")

words = sentence.split()

sentence = ' '.join(word.capitalize() for word in words)

print("result sentence:", sentence)
