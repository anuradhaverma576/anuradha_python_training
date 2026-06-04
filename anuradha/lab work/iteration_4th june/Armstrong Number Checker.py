# Armstrong Number Checker

num = int(input("Enter a number: "))

temp = num
sum = 0

# Calculate sum of cube of digits
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10

# Check Armstrong Number
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")