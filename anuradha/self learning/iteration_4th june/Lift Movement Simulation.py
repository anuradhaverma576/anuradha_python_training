current_floor = 0
total = 0

while True:
    floor = int(input("Enter Destination Floor: "))

    if floor == -1:
        break

    travelled = abs(floor - current_floor)

    print("Travelled:", travelled, "floors")

    total += travelled
    current_floor = floor

print("Total Travelled =", total)