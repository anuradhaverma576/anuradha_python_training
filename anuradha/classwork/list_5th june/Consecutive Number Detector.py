numbers = [4, 5, 6, 10, 11, 15, 16, 17]

consecutive_pairs = []

for i in range(len(numbers) - 1):
    if numbers[i] + 1 == numbers[i + 1]:
        print(numbers[i], "and", numbers[i + 1], "are consecutive")
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

print("Consecutive Pairs:", consecutive_pairs)