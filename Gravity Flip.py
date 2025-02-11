# Read the number of columns
n = int(input())

# Read the list of cube counts in each column
cubes = list(map(int, input().split()))

# Sort the cube counts in non-decreasing order
cubes_sorted = sorted(cubes)

# Print the sorted cube counts separated by spaces
print(" ".join(map(str, cubes_sorted)))