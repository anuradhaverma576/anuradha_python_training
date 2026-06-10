# Product Review Analyzer

# Taking review input from user
review = input("Enter Review: ")

# Split review into words
words = review.split()

# Count total words
total_words = len(words)

# Create empty dictionary for frequency
frequency = {}

# Count word frequency
for word in words:

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Variables for most frequent word
most_word = ""
highest_frequency = 0

# Find most frequent word
for key in frequency:

    if frequency[key] > highest_frequency:
        highest_frequency = frequency[key]
        most_word = key

# Create list for words appearing once
once_words = []

# Find words appearing once
for key in frequency:

    if frequency[key] == 1:
        once_words.append(key)

# Create list for words greater than 5 characters
greater_words = []

# Check word length
for word in words:

    if len(word) > 5:
        greater_words.append(word)

# Reverse word order
reverse_words = words[::-1]

# Create unique word list
unique_words = list(frequency.keys())

# Display output
print("\nTotal Words:", total_words)

print("\nWord Frequencies:")
for key in frequency:
    print(key, "->", frequency[key])

print("\nMost Frequent Word:", most_word)

print("\nWords Appearing Once:")
print(once_words)

print("\nWords Greater Than 5 Characters:")
print(greater_words)

print("\nWords In Reverse Order:")
print(reverse_words)

print("\nUnique Words:")
print(unique_words)