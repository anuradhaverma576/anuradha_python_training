# ATM Simulation System

balance = 10000

while True:
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

    elif choice == 2:
        deposit = float(input("Enter amount to deposit: ₹"))
        
        if deposit > 0:
            balance += deposit
            print("₹", deposit, "deposited successfully.")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid deposit amount!")

    elif choice == 3:
        withdraw = float(input("Enter amount to withdraw: ₹"))

        if withdraw > balance:
            print("Insufficient Balance!")
        elif withdraw <= 0:
            print("Invalid withdrawal amount!")
        else:
            balance -= withdraw
            print("₹", withdraw, "withdrawn successfully.")
            print("Remaining Balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid Choice! Please select a valid option.")