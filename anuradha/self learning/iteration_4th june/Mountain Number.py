n = input("Enter a number: ")

i = 0

# Increasing part
while i < len(n)-1 and n[i] < n[i+1]:
    i += 1

# Decreasing part
while i < len(n)-1 and n[i] > n[i+1]:
    i += 1

if i == len(n)-1:
    print("Mountain Number")
else:
    print("Not a Mountain Number")