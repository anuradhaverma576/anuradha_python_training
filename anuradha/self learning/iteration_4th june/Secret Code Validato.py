n = input("Enter 6-digit code: ")

if len(n) == 6:
    first = int(n[0]) + int(n[1]) + int(n[2])
    last = int(n[3]) + int(n[4]) + int(n[5])

    if first == last:
        print("Valid Code")
    else:
        print("Invalid Code")
else:
    print("Invalid Code")