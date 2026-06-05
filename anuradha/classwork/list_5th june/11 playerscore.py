players = []

# Input scores of 11 players
for i in range(1, 12):
    score = int(input(f"Enter score of Player {i}: "))
    players.append(score)

# Display all player scores
print("\nPlayer Scores:")
for i in range(11):
    print(f"Player {i+1} Score = {players[i]}")