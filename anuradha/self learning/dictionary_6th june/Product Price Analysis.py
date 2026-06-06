prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Products costing more than 5000
print("Products costing more than ₹5000:")

for item in prices:
    if prices[item] > 5000:
        print(item, prices[item])

# Products less than 3000
count = 0

for item in prices:
    if prices[item] < 3000:
        count += 1

print("\nProducts costing less than ₹3000:", count)

# Most expensive product
highest = max(prices, key=prices.get)

print("\nMost Expensive Product:")
print(highest, prices[highest])

# Products between 2000 and 10000
product_list = []

for item in prices:
    if 2000 <= prices[item] <= 10000:
        product_list.append(item)

print("\nProducts priced between ₹2000 and ₹10000:")
print(product_list)

# Total value
total = 0

for item in prices:
    total += prices[item]

print("\nTotal Value of Products:", total)