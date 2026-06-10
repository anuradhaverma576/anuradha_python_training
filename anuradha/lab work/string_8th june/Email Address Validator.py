# Email Address Validator

# Taking email input from user
email = input("Enter Email Address: ")

# Split username and domain part
parts = email.split("@")

# Initialize variables
username = ""
domain = ""
extension = ""

# Check if email has exactly one @
if len(parts) == 2:

    # Extract username
    username = parts[0]

    # Split domain and extension
    domain_parts = parts[1].split(".")

    # Check if dot exists
    if len(domain_parts) >= 2:
        domain = domain_parts[0]
        extension = domain_parts[-1]

# Count digits in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

# Count special characters
special_count = 0

for ch in email:
    if not ch.isalnum():
        special_count += 1

# Validate email
valid = False

if email.count("@") == 1:

    at_index = email.index("@")

    # Check dot after @
    if "." in email[at_index:]:
        valid = True

# Display output
print("\nEmail:", email)

print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)

print("\nDigits Found:", digit_count)
print("Special Characters Found:", special_count)

# Display email status
if valid:
    print("\nEmail Status: Valid")
else:
    print("\nEmail Status: Invalid")