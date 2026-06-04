total_bill = 0

while True:
    price = int(input("Enter Item Price: "))

    if price == 0:
        break

    total_bill = total_bill + price

print("Total Bill Amount: ₹", total_bill)