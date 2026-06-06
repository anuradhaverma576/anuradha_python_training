slots = [1, 0, 1, 1, 0, 0, 1, 0]

# Count occupied and available slots
occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied Slots:", occupied)
print("Available Slots:", available)

# First available slot
for i in range(len(slots)):
    if slots[i] == 0:
        print("\nFirst Available Slot:", i + 1)
        break

# Display all available slot numbers
print("\nAvailable Slot Numbers:")
for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)

# Check occupancy exceeds 75%
percentage = (occupied / len(slots)) * 100

print("\nOccupancy Percentage:", percentage)

if percentage > 75:
    print("Parking occupancy exceeds 75%")
else:
    print("Parking occupancy does not exceed 75%")