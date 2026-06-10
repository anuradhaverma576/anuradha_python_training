# Email Validation & Domain Analytics System

# Dictionary to count domains
domain_count = {}

# List to store invalid emails
invalid_emails = []

# Total emails to input
total_emails = 20

# Loop for 20 emails
for i in range(total_emails):

    print("\nEnter Email", i + 1)
    email = input("Enter email: ")

    print("\n------ Email Analysis ------")

    # Check validity conditions
    valid = True

    if email.count("@") != 1:
        valid = False

    if "." not in email:
        valid = False

    if " " in email:
        valid = False

    # If email is valid
    if valid:

        # Split username and domain
        parts = email.split("@")
        username = parts[0]
        domain = parts[1]

        # Extract extension
        extension = domain.split(".")[-1]

        # Count digits in username
        digit_count = 0
        for ch in username:
            if ch.isdigit():
                digit_count += 1

        # Count special characters
        special_count = 0
        for ch in email:
            if not ch.isalnum() and ch not in "@.":
                special_count += 1

        # Count domain frequency
        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1

        # Display analysis
        print("Username:", username)
        print("Domain:", domain)
        print("Extension:", extension)
        print("Digits in Username:", digit_count)
        print("Special Characters:", special_count)
        print("Email Status: Valid")

    else:
        print("Email Status: Invalid")
        invalid_emails.append(email)

# Display invalid emails
print("\n------ Invalid Emails ------")

if len(invalid_emails) == 0:
    print("No Invalid Emails")
else:
    for email in invalid_emails:
        print(email)

# Domain Report
print("\n====== Domain Report ======")

for domain in domain_count:
    print(domain, "->", domain_count[domain], "users")