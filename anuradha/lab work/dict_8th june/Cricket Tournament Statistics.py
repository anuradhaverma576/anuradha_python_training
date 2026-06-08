# Dictionary storing player runs
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")

for player in runs:
    if runs[player] > 500:
        print(player)

# Find Orange Cap winner
winner = ""
highest_runs = 0

for player in runs:
    if runs[player] > highest_runs:
        highest_runs = runs[player]
        winner = player

print("\nOrange Cap Winner:", winner, "(", highest_runs, ")", sep="")

# Find lowest scorer
lowest_player = ""
lowest_runs = 99999

for player in runs:
    if runs[player] < lowest_runs:
        lowest_runs = runs[player]
        lowest_player = player

print("Lowest Scorer:", lowest_player, "(", lowest_runs, ")", sep="")

# Calculate total runs scored
total_runs = 0

for player in runs:
    total_runs += runs[player]

print("Total Tournament Runs:", total_runs)

# Create list of players scoring below 400
below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("Players Scoring Below 400:")
print(below_400)

# Count players scoring between 400 and 600
count = 0

for player in runs:
    if runs[player] >= 400 and runs[player] <= 600:
        count += 1

print("Players Between 400 and 600 Runs:", count)