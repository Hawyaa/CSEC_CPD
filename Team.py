# Read the number of problems
n = int(input())

# Initialize a counter for the number of problems they will implement
count = 0

# Iterate through each problem
for _ in range(n):
    # Read the confidence of Petya, Vasya, and Tonya for the current problem
    petya, vasya, tonya = map(int, input().split())
    
    # Check if at least two of them are confident
    if petya + vasya + tonya >= 2:
        count += 1  # Increment the counter

# Print the total number of problems they will implement
print(count)