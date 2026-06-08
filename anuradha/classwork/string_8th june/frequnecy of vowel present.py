# wap to find out input a senetnce and display the frequnecy of vowel present in that senetece ignoring the given sentence

s = input("Enter a sentence: ")

count = 0

for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels =", count)
