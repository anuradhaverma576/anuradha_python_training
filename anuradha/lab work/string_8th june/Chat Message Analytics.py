# Chat Message Analytics

# Taking message input from user
message = input("Enter Message: ")

# Count total characters
total_characters = len(message)

# Split sentence into words
words = message.split()

# Count total words
total_words = len(words)

# Assume first word as longest and shortest
longest_word = words[0]
shortest_word = words[0]

# Loop to find longest and shortest word
for word in words:

    # Find longest word
    if len(word) > len(longest_word):
        longest_word = word

    # Find shortest word
    if len(word) < len(shortest_word):
        shortest_word = word

# Count occurrence of Python
python_count = words.count("Python")

# Empty list for words > 4 characters
greater_words = []

# Check word length
for word in words:
    if len(word) > 4:
        greater_words.append(word)

# Empty list for vowel words
vowel_words = []

# Find words starting with vowels
for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

# Variables for vowels and consonants
vowels = 0
consonants = 0

# Loop through each character
for ch in message.lower():

    # Check alphabet
    if ch.isalpha():

        # Check vowels
        if ch in "aeiou":
            vowels += 1

        # Otherwise consonant
        else:
            consonants += 1

# Display results
print("\nMessage:", message)

print("\nTotal Characters:", total_characters)
print("Total Words:", total_words)

print("\nLongest Word:", longest_word)
print("Shortest Word:", shortest_word)

print("\nOccurrences of Python:", python_count)

print("\nWords Longer Than 4 Characters:")
print(greater_words)

print("\nWords Starting With Vowel:")
print(vowel_words)

print("\nVowels:", vowels)
print("Consonants:", consonants)