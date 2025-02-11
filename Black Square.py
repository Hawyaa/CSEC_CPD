# Read the four calorie values for each strip
a = list(map(int, input().split()))
# Read the string representing the game's process
s = input().strip()

total = 0

# Iterate through each character in the string
for c in s:
    # Convert character to integer and adjust index to 0-based
    index = int(c) - 1
    # Add the corresponding calorie value to the total
    total += a[index]

# Print the total calories
print(total)