# Read the initial weights of Limak and Bob
a, b = map(int, input().split())

# Initialize the year counter
years = 0

# Simulate the weight changes year by year
while a <= b:
    a *= 3  # Limak's weight triples
    b *= 2  # Bob's weight doubles
    years += 1  # Increment the year counter

# Output the number of years it took for Limak to become larger than Bob
print(years)