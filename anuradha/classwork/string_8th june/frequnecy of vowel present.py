# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Convert sentence to lowercase
sentence = sentence.lower()

# Variables to count vowels
a = 0
e = 0
i = 0
o = 0
u = 0

# Check each character
for ch in sentence:
    
    if ch == 'a':
        a = a + 1
    elif ch == 'e':
        e = e + 1
    elif ch == 'i':
        i = i + 1
    elif ch == 'o':
        o = o + 1
    elif ch == 'u':
        u = u + 1

# Display frequency of vowels
print("Frequency of vowels:")
print("A =", a)
print("E =", e)
print("I =", i)
print("O =", o)
print("U =", u)