n = input("Enter a number: ")

mid = len(n) // 2

left = n[:mid]
right = n[mid:]

if left == right:
    print("Mirror Number")
else:
    print("Not a Mirror Number")