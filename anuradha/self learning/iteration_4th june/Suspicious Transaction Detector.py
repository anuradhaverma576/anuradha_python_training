high = 0
low = 0
total = 0

while True:
    amount = int(input("Enter transaction amount: "))

    if amount == -1:
        break

    total += amount

    if amount > 50000:
        high += 1

    if amount < 1000:
        low += 1

print("Transactions above 50000 =", high)
print("Transactions below 1000 =", low)
print("Total Transaction Amount =", total)