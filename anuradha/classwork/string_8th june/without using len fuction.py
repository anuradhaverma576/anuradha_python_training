# write aprogarm t input a string or semntece from user and count the number of char present in it without using len fuction
# Input a string or sentence from the user
text = input("Enter a string or sentence: ")

# Variable to count characters
count = 0

# Loop through each character
for ch in text:
    count = count + 1

# Display total number of characters
print("Total number of characters:", count)