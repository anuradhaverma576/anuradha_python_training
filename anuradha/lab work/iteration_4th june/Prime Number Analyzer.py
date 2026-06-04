# Prime Number Analyzer

num = int(input("Enter a number: "))

factors = []

# Find factors
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

# Check prime number
if len(factors) == 2:
    print(num, "is a Prime Number")
else:
    print("Factors:", end=" ")
    for factor in factors:
        print(factor, end=" ")
    print()
    print(num, "is not a Prime Number")