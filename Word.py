# Read the word
word = input().strip()

# Count the number of lowercase and uppercase letters
lower_count = sum(1 for char in word if char.islower())
upper_count = sum(1 for char in word if char.isupper())

# Determine the correct case
if upper_count > lower_count:
    corrected_word = word.upper()
else:
    corrected_word = word.lower()

# Print the corrected word
print(corrected_word)