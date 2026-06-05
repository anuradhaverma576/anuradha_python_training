stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = 0
restock = []
available = 0
healthy_stock = []

for item in stock:
    # Out of stock
    if item == 0:
        out_of_stock += 1

    # Restocking required
    if item < 10:
        restock.append(item)

    # Available products
    if item > 0:
        available += 1

    # Healthy stock
    if item >= 15:
        healthy_stock.append(item)

print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock)
print("Available Products:", available)
print("Healthy Stock:", healthy_stock)