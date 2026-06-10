# Username Generator System

# Taking full name input
name = input("Enter Full Name: ")

# Remove spaces
username = name.replace(" ", "")

# Convert to lowercase
username = username.lower()

# Add current year
username = username + "2026"

# Check username length
if len(username) > 12:
    username = username[:12]

# Variables for vowels and consonants
vowels = 0
consonants = 0

# Count vowels and consonants
for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Display output
print("\nOriginal Name:", name)

print("\nGenerated Username:")
print(username)

print("\nUsername Length:", len(username))

print("\nVowels:", vowels)
print("Consonants:", consonants)

print("\nStatus: Username Generated Successfully")