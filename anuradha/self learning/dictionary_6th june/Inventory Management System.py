inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Products with stock less than 10
print("Stock less than 10:")

for item in inventory:
    if inventory[item] < 10:
        print(item)

# Products having stock more than 50
count = 0

for item in inventory:
    if inventory[item] > 50:
        count += 1

print("\nProducts with stock > 50:", count)

# Minimum stock product
minimum = min(inventory, key=inventory.get)

print("\nMinimum Stock Product:")
print(minimum, inventory[minimum])

# Restocking list
restock = []

for item in inventory:
    if inventory[item] < 20:
        restock.append(item)

print("\nProducts requiring restocking:")
print(restock)

# Total inventory count
total = 0

for item in inventory:
    total += inventory[item]

print("\nTotal Inventory Count:", total)