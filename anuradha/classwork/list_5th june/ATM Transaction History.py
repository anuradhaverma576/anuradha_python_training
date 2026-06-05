transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0
deposits = []
withdrawals = []

largest_deposit = 0
largest_withdrawal = transactions[1]

for amount in transactions:
    balance += amount

    if amount > 0:
        deposits.append(amount)

        if amount > largest_deposit:
            largest_deposit = amount

    else:
        withdrawals.append(amount)

        if amount < largest_withdrawal:
            largest_withdrawal = amount

print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)