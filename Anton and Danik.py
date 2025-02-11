# Read the number of games
n = int(input())

# Read the outcomes of the games
s = input()

# Count the wins
anton_wins = s.count('A')
danik_wins = s.count('D')

# Determine the result
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")