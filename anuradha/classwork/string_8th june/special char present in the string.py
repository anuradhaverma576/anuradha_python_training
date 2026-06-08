# write a program to input a sentence from user and count the number of special char present in the string
# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Variable to count special characters
count = 0

# Check each character in the sentence
for ch in sentence:
    
    # Count if character is not alphabet, digit, or space
    if not ch.isalnum() and ch != " ":
        count = count + 1

# Display result
print("Number of special characters:", count)