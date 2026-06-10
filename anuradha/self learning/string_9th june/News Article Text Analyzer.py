# News Article Text Analyzer

# Paragraph (Sample News Article)
article = """
Technology is changing the world rapidly. Artificial intelligence is helping
businesses improve productivity and efficiency. Many companies are investing
in automation to reduce workload and increase accuracy. Education systems
are also using digital platforms to improve learning experiences. Students
can now access online classes, digital books, and learning resources easily.
Healthcare industries are improving patient treatment with advanced machines.
Doctors can diagnose diseases more accurately with modern technology.
Governments are also encouraging digital transformation in many sectors.
People communicate faster through social media and messaging applications.
Businesses use online advertising to attract more customers. Scientists are
researching renewable energy to reduce pollution and climate change. News
organizations use digital tools to deliver information quickly. Security
systems are becoming stronger with cyber protection methods. Technology is
making transportation smarter and safer. Electric vehicles are reducing fuel
consumption and environmental pollution. Researchers continue to discover
new methods to solve global problems using science and technology.
"""

# Convert paragraph into lowercase words
words = article.lower().split()

# Count total characters
total_characters = len(article)

# Count total words
total_words = len(words)

# Count total sentences
sentences = article.count('.') + article.count('!') + article.count('?')

# Count vowels and consonants
vowels = 0
consonants = 0

for ch in article.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Find longest and shortest word
longest_word = words[0]
shortest_word = words[0]

for word in words:
    clean_word = word.strip(".,!?")

    if len(clean_word) > len(longest_word):
        longest_word = clean_word

    if len(clean_word) < len(shortest_word):
        shortest_word = clean_word

# Create dictionary for word frequencies
word_frequency = {}

for word in words:
    clean_word = word.strip(".,!?")

    if clean_word in word_frequency:
        word_frequency[clean_word] += 1
    else:
        word_frequency[clean_word] = 1

# Find most frequent word
most_frequent_word = ""
highest_count = 0

for word in word_frequency:
    if word_frequency[word] > highest_count:
        highest_count = word_frequency[word]
        most_frequent_word = word

# Display words appearing only once
print("Words Appearing Only Once")
print("-" * 30)

for word in word_frequency:
    if word_frequency[word] == 1:
        print(word)

# Display words appearing more than 5 times
print("\nWords Appearing More Than 5 Times")
print("-" * 35)

for word in word_frequency:
    if word_frequency[word] > 5:
        print(word)

# Count words starting with each alphabet
alphabet_count = {}

for word in word_frequency:
    first_letter = word[0]

    if first_letter in alphabet_count:
        alphabet_count[first_letter] += 1
    else:
        alphabet_count[first_letter] = 1

# Display all unique words
print("\nUnique Words")
print("-" * 20)

for word in word_frequency:
    print(word)

# Generate Complete Text Summary
print("\nText Summary Report")
print("-" * 30)

print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Total Sentences:", sentences)
print("Total Vowels:", vowels)
print("Total Consonants:", consonants)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Most Frequent Word:", most_frequent_word)
print("Vocabulary Size:", len(word_frequency))

# Average word length
total_length = 0

for word in words:
    total_length += len(word.strip(".,!?"))

average_word_length = total_length / total_words

print("Average Word Length:", round(average_word_length, 2))