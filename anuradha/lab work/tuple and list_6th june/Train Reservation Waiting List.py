passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# Waiting-list passengers
print("Waiting List Passengers:")

for p in passengers:
    if p[1] == "Waiting":
        print(p[0])

# Count confirmed and waiting
confirmed = 0
waiting = 0

for p in passengers:
    if p[1] == "Confirmed":
        confirmed += 1
    else:
        waiting += 1

print("\nConfirmed:", confirmed)
print("Waiting:", waiting)

# Specific passenger confirmation
name = input("\nEnter passenger name: ")
found = False

for p in passengers:
    if p[0] == name and p[1] == "Confirmed":
        found = True
        break

if found:
    print("Confirmed Ticket Found")
else:
    print("No Confirmed Ticket")

# Separate lists
confirmed_list = []
waiting_list = []

for p in passengers:
    if p[1] == "Confirmed":
        confirmed_list.append(p[0])
    else:
        waiting_list.append(p[0])

print("\nConfirmed Passengers:", confirmed_list)
print("Waiting Passengers:", waiting_list)