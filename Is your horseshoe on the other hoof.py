# Read the four horseshoe colors
horseshoes = list(map(int, input().split()))

# Calculate the number of unique colors using a set
unique_colors = len(set(horseshoes))

# The answer is 4 minus the number of unique colors
print(4 - unique_colors)