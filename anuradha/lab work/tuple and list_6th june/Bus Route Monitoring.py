passengers = [12, 18, 25, 30, 28, 15, 8]

# Busiest stop
highest = passengers[0]
stop = 1

for i in range(len(passengers)):
    if passengers[i] > highest:
        highest = passengers[i]
        stop = i + 1

print("Busiest Stop:", stop)

# Stops with fewer than 10 passengers
print("\nStops with fewer than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print("Stop", i + 1)

# Average passengers
total = 0

for p in passengers:
    total += p

average = total / len(passengers)

print("\nAverage Passengers:", average)

# Any stop exceeded 25 passengers
found = False

for p in passengers:
    if p > 25:
        found = True
        break

if found:
    print("\nA stop exceeded 25 passengers")
else:
    print("\nNo stop exceeded 25 passengers")