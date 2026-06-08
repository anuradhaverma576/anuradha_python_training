# Dictionary storing product sales data
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product in sales:
    if sales[product] > 20:
        print(product)

# Find best-selling product
best_product = ""
highest_sale = 0

for product in sales:
    if sales[product] > highest_sale:
        highest_sale = sales[product]
        best_product = product

print("\nBest Selling Product:", best_product, "(", highest_sale, ")", sep="")

# Find least-selling product
least_product = ""
lowest_sale = 99999

for product in sales:
    if sales[product] < lowest_sale:
        lowest_sale = sales[product]
        least_product = product

print("Least Selling Product:", least_product, "(", lowest_sale, ")", sep="")

# Calculate total products sold
total_sales = 0

for product in sales:
    total_sales += sales[product]

print("Total Units Sold:", total_sales)

# Create list of products requiring promotion
promotion_list = []

for product in sales:
    if sales[product] < 15:
        promotion_list.append(product)

print("Products Requiring Promotion:")
print(promotion_list)

# Count products having sales between 10 and 30
count = 0

for product in sales:
    if sales[product] >= 10 and sales[product] <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)