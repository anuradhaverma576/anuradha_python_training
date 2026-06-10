# Password Security Analyzer

# Counters for final report
strong_count = 0
medium_count = 0
weak_count = 0

# Total passwords analyzed
total_passwords = 15

# Loop to input at least 15 passwords
for i in range(total_passwords):

    print("\nEnter Password", i + 1)
    password = input("Enter password: ")

    # Initialize counters
    upper = 0
    lower = 0
    digit = 0
    special = 0
    vowels = 0
    consonants = 0
    repeated_char = ""

    # Count uppercase, lowercase, digits, special characters
    for ch in password:

        if ch.isupper():
            upper += 1

        elif ch.islower():
            lower += 1

        elif ch.isdigit():
            digit += 1

        else:
            special += 1

    # Check vowels and consonants
    for ch in password:

        if ch.isalpha():

            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1

    # Check minimum length
    if len(password) >= 8:
        length_check = "Valid Length"
    else:
        length_check = "Invalid Length"

    # Check spaces
    if " " in password:
        space_check = "Spaces Present"
    else:
        space_check = "No Spaces"

    # Password strength checking
    if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
        strength = "Strong"
        strong_count += 1

    elif len(password) >= 8 and (upper > 0 or lower > 0) and digit > 0:
        strength = "Medium"
        medium_count += 1

    else:
        strength = "Weak"
        weak_count += 1

    # Display repeated characters
    checked = ""

    for ch in password:
        count = 0

        for x in password:
            if ch == x:
                count += 1

        if count > 1 and ch not in checked:
            repeated_char += ch + " "
            checked += ch

    # Find most frequent character
    max_count = 0
    most_frequent = ""

    for ch in password:
        count = 0

        for x in password:
            if ch == x:
                count += 1

        if count > max_count:
            max_count = count
            most_frequent = ch

    # Display password analysis
    print("\n------ Password Analysis ------")
    print("Password:", password)
    print("Uppercase Letters:", upper)
    print("Lowercase Letters:", lower)
    print("Digits:", digit)
    print("Special Characters:", special)
    print("Length Check:", length_check)
    print("Space Check:", space_check)
    print("Password Strength:", strength)
    print("Repeated Characters:", repeated_char)

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Most Frequent Character:", most_frequent)

# Final Report
print("\n========== Security Report ==========")
print("Total Passwords Analyzed:", total_passwords)
print("Strong Passwords:", strong_count)
print("Medium Passwords:", medium_count)
print("Weak Passwords:", weak_count)