correct_pin = 1234
pin = 0

while pin != correct_pin:
    pin = int(input("Enter PIN: "))

    if pin != correct_pin:
        print("Incorrect PIN. Try Again.")

print("Access Granted.")