# Read the number of stones
n = int(input())

# Read the string representing the colors of the stones
s = input().strip()

# Initialize the count of stones to remove
remove_count = 0

# Iterate through the string and count consecutive stones with the same color
for i in range(n - 1):
    if s[i] == s[i + 1]:
        remove_count += 1

# Print the result
print(remove_count)