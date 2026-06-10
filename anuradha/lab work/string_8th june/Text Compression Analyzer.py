# Text Compression Analyzer

# Taking compressed text input
text = input("Enter Text: ")

# Empty dictionary for frequency
frequency = {}

# Count character frequency
for ch in text:

    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

# Display frequencies
print("\nCharacter Frequencies:")
for key in frequency:
    print(key, "->", frequency[key])

# Unique characters
unique_characters = list(frequency.keys())

print("\nUnique Characters:")
print(unique_characters)

# Find most frequent character
most_character = ""
highest = 0

for key in frequency:

    if frequency[key] > highest:
        highest = frequency[key]
        most_character = key

print("\nMost Frequent Character:", most_character)

# Create compressed output
compressed = ""

count = 1

for i in range(len(text)-1):

    if text[i] == text[i+1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

# Add last character
compressed += text[-1] + str(count)

# Calculate lengths
original_length = len(text)
compressed_length = len(compressed)

# Compression ratio
ratio = (compressed_length / original_length) * 100

# Display output
print("\nCompressed Output:")
print(compressed)

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)

print("\nCompression Ratio:", round(ratio, 2), "%")