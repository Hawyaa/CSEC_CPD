# Read the two strings
string1 = input().strip()
string2 = input().strip()

# Convert both strings to lowercase (or uppercase) for case-insensitive comparison
string1_lower = string1.lower()
string2_lower = string2.lower()

# Compare the two strings lexicographically
if string1_lower < string2_lower:
    print(-1)
elif string1_lower > string2_lower:
    print(1)
else:
    print(0)