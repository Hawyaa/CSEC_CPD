# Read the number of magnets
n = int(input())

# Read the configurations of the magnets
magnets = [input().strip() for _ in range(n)]

# Initialize the group counter
group_count = 1  # At least one group exists

# Iterate through the magnets and count groups
for i in range(1, n):
    if magnets[i] != magnets[i - 1]:
        group_count += 1

# Print the number of groups
print(group_count)