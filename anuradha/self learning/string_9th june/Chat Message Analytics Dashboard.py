# Chat Message Analytics Dashboard

# List to store messages
messages = []

# Dictionary for all word frequencies
word_frequency = {}

# Input 20 messages
for i in range(20):
    msg = input("Enter chat message: ")
    messages.append(msg)

# Variables for report
longest_message = messages[0]
shortest_message = messages[0]
total_words_all = 0
most_used_word = ""

# Analyze each message
for msg in messages:

    print("\n------ Message Analysis ------")

    words = msg.split()

    # Total words
    total_words = len(words)
    total_words_all += total_words

    # Total characters
    total_characters = len(msg)

    # Vowels and consonants
    vowels = 0
    consonants = 0

    for ch in msg:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    # Longest and shortest word
    longest_word = words[0]
    shortest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

    # Word frequency
    msg_frequency = {}

    for word in words:
        word = word.lower()

        if word in msg_frequency:
            msg_frequency[word] += 1
        else:
            msg_frequency[word] = 1

        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    # Repeated words
    repeated_words = []

    for word in msg_frequency:
        if msg_frequency[word] > 1:
            repeated_words.append(word)

    # Words starting with vowels
    vowel_words = []

    for word in words:
        if word[0].lower() in "aeiou":
            vowel_words.append(word)

    # Words longer than 5 characters
    long_words = []

    for word in words:
        if len(word) > 5:
            long_words.append(word)

    # Display analysis
    print("Total Words:", total_words)
    print("Total Characters:", total_characters)
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Longest Word:", longest_word)
    print("Shortest Word:", shortest_word)
    print("Repeated Words:", repeated_words)
    print("Words Starting with Vowels:", vowel_words)
    print("Words Longer than 5 Characters:", long_words)
    print("Word Frequency:", msg_frequency)

# Longest and shortest message
for msg in messages:
    if len(msg) > len(longest_message):
        longest_message = msg

    if len(msg) < len(shortest_message):
        shortest_message = msg

# Most frequently used word
max_count = 0

for word in word_frequency:
    if word_frequency[word] > max_count:
        max_count = word_frequency[word]
        most_used_word = word

# Final Report
print("\n====== Chat Analytics Report ======")
print("Most Frequently Used Word:", most_used_word)
print("Longest Message:", longest_message)
print("Shortest Message:", shortest_message)
print("Average Words Per Message:", total_words_all / 20)