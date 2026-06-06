scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Players scoring 50 or more
print("Players scoring 50 or more:")

for player in scores:
    if scores[player] >= 50:
        print(player, scores[player])

# Count centuries
centuries = 0

for player in scores:
    if scores[player] >= 100:
        centuries += 1

print("\nNumber of Centuries:", centuries)

# Highest scorer
highest = max(scores, key=scores.get)

print("\nHighest Scorer:")
print(highest, scores[highest])

# Players scoring below 30
low_scores = []

for player in scores:
    if scores[player] < 30:
        low_scores.append(player)

print("\nPlayers scoring below 30:")
print(low_scores)

# Players scoring between 50 and 99
count = 0

for player in scores:
    if 50 <= scores[player] <= 99:
        count += 1

print("\nPlayers scoring between 50 and 99:", count)