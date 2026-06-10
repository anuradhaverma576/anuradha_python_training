# Employee ID Validation and Analysis System

# Taking employee ID input from the user
emp_id = input("Enter Employee ID: ")

# Initializing variables to count uppercase letters and digits
uppercase_count = 0
digit_count = 0

# Creating an empty list to store digits
digit_list = []

# Variable to store sum of digits
digit_sum = 0

# Loop through every character in employee ID
for ch in emp_id:

    # Check if character is uppercase
    if ch.isupper():
        uppercase_count += 1

    # Check if character is a digit
    if ch.isdigit():
        digit_count += 1

        # Add digit to list
        digit_list.append(int(ch))

        # Add digit to sum
        digit_sum += int(ch)

# Extract joining year (4 digits after EMP)
joining_year = emp_id[3:7]

# Extract employee name
employee_name = emp_id[7:-3]

# Variable to check validity
valid = False

# Check if ID starts with EMP
if emp_id.startswith("EMP"):

    # Check if joining year contains exactly 4 digits
    if joining_year.isdigit() and len(joining_year) == 4:

        # Check if last 3 characters are digits
        if emp_id[-3:].isdigit():
            valid = True

# Display employee ID
print("\nEmployee ID:", emp_id)

# Display uppercase and digit count
print("Uppercase Letters:", uppercase_count)
print("Digits:", digit_count)

# Display joining year and employee name
print("\nJoining Year:", joining_year)
print("Employee Name:", employee_name)

# Display list of digits
print("\nDigit List:", digit_list)

# Display sum of digits
print("Sum of Digits:", digit_sum)

# Check validity and display result
if valid:
    print("\nID Status: Valid")
else:
    print("\nID Status: Invalid")