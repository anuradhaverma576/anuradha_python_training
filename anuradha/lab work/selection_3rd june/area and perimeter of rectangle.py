# Program to calculate area and perimeter of rectangle

length = float(input("Enter Length of Rectangle: "))
breadth = float(input("Enter Breadth of Rectangle: "))

# Calculate area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Display result
print("Area of Rectangle =", area)
print("Perimeter of Rectangle =", perimeter)