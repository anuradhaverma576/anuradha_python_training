# Vehicle Number Plate Verification

# Taking vehicle number input from user
vehicle = input("Enter Vehicle Number: ")

# Extract state code (first 2 characters)
state_code = vehicle[:2]

# Extract district code (next 2 characters)
district_code = vehicle[2:4]

# Extract vehicle series (next 2 characters)
series = vehicle[4:6]

# Extract vehicle number (last 4 digits)
vehicle_number = vehicle[6:]

# Variables to count letters and digits
letter_count = 0
digit_count = 0

# Loop through each character
for ch in vehicle:

    # Count letters
    if ch.isalpha():
        letter_count += 1

    # Count digits
    elif ch.isdigit():
        digit_count += 1

# Variable for validation
valid = False

# Check format of number plate
if vehicle[:2].isalpha():

    if vehicle[2:4].isdigit():

        if vehicle[4:6].isalpha():

            if vehicle[6:].isdigit() and len(vehicle[6:]) == 4:
                valid = True

# Display output
print("\nVehicle Number:", vehicle)

print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)

print("\nTotal Letters:", letter_count)
print("Total Digits:", digit_count)

# Display status
if valid:
    print("\nVehicle Number Status: Valid")
else:
    print("\nVehicle Number Status: Invalid")