# Dictionary storing electricity units consumed
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house in units:
    if units[house] > 400:
        print(house)

# Find highest-consuming house
highest_house = ""
highest_units = 0

for house in units:
    if units[house] > highest_units:
        highest_units = units[house]
        highest_house = house

print("\nHighest Consumption:", highest_house, "(", highest_units, "units)", sep="")

# Find lowest-consuming house
lowest_house = ""
lowest_units = 99999

for house in units:
    if units[house] < lowest_units:
        lowest_units = units[house]
        lowest_house = house

print("Lowest Consumption:", lowest_house, "(", lowest_units, "units)", sep="")

# Calculate total units consumed
total_units = 0

for house in units:
    total_units += units[house]

print("Total Units Consumed:", total_units)

# Create separate lists
low = []
medium = []
high = []

for house in units:
    consumption = units[house]

    if consumption < 200:
        low.append(house)

    elif consumption <= 400:
        medium.append(house)

    else:
        high.append(house)

print("Low Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

# Count houses eligible for energy-saving campaign
count = 0

for house in units:
    if units[house] > 300:
        count += 1

print("Eligible for Energy-Saving Campaign:", count)