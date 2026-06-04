n = int(input("Enter number of racers: "))

fastest = float('inf')
slowest = float('-inf')

fast_pos = 0
slow_pos = 0

for i in range(1, n + 1):
    time = int(input("Enter lap time: "))

    if time < fastest:
        fastest = time
        fast_pos = i

    if time > slowest:
        slowest = time
        slow_pos = i

print("Fastest Racer Position =", fast_pos)
print("Slowest Racer Position =", slow_pos)
print("Difference =", slowest - fastest)