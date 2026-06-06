products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

passed = 0
failed = 0

print("Failed Product IDs:")

for product in products:
    if product[1] == "Fail":
        print(product[0])
        failed += 1
    else:
        passed += 1

print("\nPassed Products:", passed)
print("Failed Products:", failed)

# Pass percentage
percentage = (passed / len(products)) * 100

print("\nPass Percentage:", percentage)

# Stop checking if 3 failures found
fail_count = 0

for product in products:
    if product[1] == "Fail":
        fail_count += 1

    if fail_count == 3:
        print("3 Failures Found")
        break