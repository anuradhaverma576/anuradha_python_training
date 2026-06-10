# Password Strength Analyzer

# Taking password input from user
password = input("Enter Password: ")

# Initializing counters
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0

# Creating empty lists
digit_list = []
special_list = []

# Loop through every character
for ch in password:

    # Check uppercase letters
    if ch.isupper():
        uppercase_count += 1

    # Check lowercase letters
    elif ch.islower():
        lowercase_count += 1

    # Check digits
    elif ch.isdigit():
        digit_count += 1

        # Store digit separately
        digit_list.append(ch)

    # Count special characters
    else:
        special_count += 1

        # Store special characters
        special_list.append(ch)

# Check password strength
if len(password) >= 8 and uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1 and special_count >= 1:
    strength = "Strong"

elif len(password) >= 6:
    strength = "Medium"

else:
    strength = "Weak"

# Display password details
print("\nPassword:", password)

print("Uppercase Letters:", uppercase_count)
print("Lowercase Letters:", lowercase_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

# Display digit list
print("\nDigits Found:", digit_list)

# Display special characters
print("Special Characters Found:", special_list)

# Display password strength
print("\nPassword Strength:", strength)