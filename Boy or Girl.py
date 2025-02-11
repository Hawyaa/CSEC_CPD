# Read the username
username = input().strip()

# Use a set to store distinct characters
distinct_chars = set(username)

# Determine the gender based on the number of distinct characters
if len(distinct_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")