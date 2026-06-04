a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# Check triangle formation
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle can be formed")

    # Specify type of triangle
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

else:
    print("Triangle cannot be formed")