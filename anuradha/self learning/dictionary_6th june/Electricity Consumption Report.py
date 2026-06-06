units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Houses consuming more than 300 units
print("Houses consuming more than 300 units:")

for house in units:
    if units[house] > 300:
        print(house, units[house])

# Houses consuming less than 200 units
count = 0

for house in units:
    if units[house] < 200:
        count += 1

print("\nHouses consuming less than 200 units:", count)

# Highest consumption
highest = max(units, key=units.get)

print("\nHighest Consumption:")
print(highest, units[highest])

# Energy-saving awareness list
campaign = []

for house in units:
    if units[house] > 400:
        campaign.append(house)

print("\nEnergy Saving Awareness Campaign:")
print(campaign)

# Categories
print("\nHouse Categories:")

for house in units:
    usage = units[house]

    if usage < 200:
        category = "Low"
    elif usage <= 350:
        category = "Medium"
    else:
        category = "High"

    print(house, "->", category)