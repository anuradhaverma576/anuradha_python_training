passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Stops having more than 20 passengers
print("Stops with more than 20 passengers:")

for stop in passengers:
    if passengers[stop] > 20:
        print(stop, passengers[stop])

# Stops fewer than 10 passengers
count = 0

for stop in passengers:
    if passengers[stop] < 10:
        count += 1

print("\nStops with fewer than 10 passengers:", count)

# Busiest stop
highest = max(passengers, key=passengers.get)

print("\nBusiest Stop:")
print(highest, passengers[highest])

# Stops needing extra bus
extra_bus = []

for stop in passengers:
    if passengers[stop] > 25:
        extra_bus.append(stop)

print("\nStops requiring extra bus:")
print(extra_bus)

# Average passengers
total = 0

for stop in passengers:
    total += passengers[stop]

average = total / len(passengers)

print("\nAverage Passengers:", average)