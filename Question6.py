import math

    # How many unique words have been used in the sentence?
sentence = "I am a teacher and I love to inspire and teach people"
print(sentence)
words = set(sentence.split())    # Using split method to split the sentence into a list of words and convert the list in to a set to get the unique words.
print(words)    # Unique words
print("Length of unique words:", len(words))      # Length of the unique words
