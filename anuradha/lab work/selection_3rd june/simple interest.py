# Program to calculate Simple Interest with valid data

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

# Validation
if principal > 0 and rate > 0 and time > 0:
    simple_interest = (principal * rate * time) / 100
    print("Simple Interest =", simple_interest)
else:
    print("Invalid Data! Please enter positive values.")