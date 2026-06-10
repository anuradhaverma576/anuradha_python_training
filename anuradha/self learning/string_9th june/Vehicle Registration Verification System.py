# Vehicle Registration Verification System

# List of 20 vehicle registration numbers
vehicles = [
    "MH12AB4589", "DL05XY9988", "KA03PQ1234", "UP32GH5678",
    "MH14CD2345", "DL09MN6789", "KA05RT3456", "UP16JK1111",
    "MH20ZX2222", "DL11AB3333", "KA09LM4444", "UP21PQ5555",
    "MH18EF6666", "DL03GH7777", "KA07JK8888", "UP45XY9999",
    "MH10AA1010", "DL08BB2020", "KA12CC3030", "UP22DD4040"
]

# Dictionary to count vehicles state-wise
state_count = {}

# List to store invalid registrations
invalid_registrations = []

print("Vehicle Registration Analysis")
print("-" * 50)

# Loop through each vehicle number
for reg in vehicles:

    print("\nRegistration Number:", reg)

    # Extract details
    state_code = reg[:2]
    district_code = reg[2:4]
    series = reg[4:6]
    vehicle_number = reg[6:]

    print("State Code:", state_code)
    print("District Code:", district_code)
    print("Series:", series)
    print("Vehicle Number:", vehicle_number)

    # Count letters and digits
    letters = 0
    digits = 0

    for ch in reg:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1

    print("Total Letters:", letters)
    print("Total Digits:", digits)

    # Validate registration format
    valid = True

    if not reg[:2].isalpha():
        valid = False
    elif not reg[2:4].isdigit():
        valid = False
    elif not reg[4:6].isalpha():
        valid = False
    elif not reg[6:].isdigit():
        valid = False
    elif len(reg) != 10:
        valid = False

    # Display validation result
    if valid:
        print("Registration Status: Valid")
    else:
        print("Registration Status: Invalid")
        invalid_registrations.append(reg)

    # Count state-wise vehicles
    if state_code in state_count:
        state_count[state_code] += 1
    else:
        state_count[state_code] = 1

# Display invalid registrations
print("\nInvalid Registrations")
print("-" * 30)

if len(invalid_registrations) == 0:
    print("No Invalid Registrations Found")
else:
    for item in invalid_registrations:
        print(item)

# State-wise report
print("\nState-wise Vehicle Report")
print("-" * 30)

for state in state_count:
    print(state, "->", state_count[state], "Vehicles")