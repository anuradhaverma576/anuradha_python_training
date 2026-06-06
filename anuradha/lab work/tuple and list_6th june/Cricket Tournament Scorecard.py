scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Count half-centuries and centuries
half_century = 0
century = 0

for score in scores:
    if score >= 100:
        century += 1
    elif score >= 50:
        half_century += 1

print("Half-centuries:", half_century)
print("Centuries:", century)

# Highest score
highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print("\nHighest Score:", highest)

# Scores below 20
print("\nScores below 20:")
for score in scores:
    if score < 20:
        print(score)

# Average score
total = 0
for score in scores:
    total += score

average = total / len(scores)

print("\nAverage Score:", average)