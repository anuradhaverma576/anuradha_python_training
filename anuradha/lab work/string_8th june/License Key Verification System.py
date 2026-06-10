# License Key Verification System

# Taking license key input
license_key = input("Enter License Key: ")

# Split key into groups
groups = license_key.split("-")

# Count total groups
group_count = len(groups)

# Variables
letter_count = 0
vowel_count = 0

# Remove hyphens
merged_key = license_key.replace("-", "")

# Count letters and vowels
for ch in merged_key:

    if ch.isalpha():
        letter_count += 1

        if ch.lower() in "aeiou":
            vowel_count += 1

# Validate format
valid = True

# Check number of groups
if group_count != 4:
    valid = False

# Check each group length
for group in groups:

    if len(group) != 4:
        valid = False

# Display output
print("\nLicense Key:")
print(license_key)

print("\nGroups:")
print(groups)

print("\nNumber of Groups:", group_count)

print("\nTotal Letters:", letter_count)
print("Total Vowels:", vowel_count)

print("\nMerged Key:")
print(merged_key)

# Display status
if valid:
    print("\nLicense Key Status: Valid")
else:
    print("\nLicense Key Status: Invalid")