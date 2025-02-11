s = input().strip()
t = input().strip()

current_position = 1  # Starting at the first stone (1-based)

for instruction in t:
    # Check the current stone's color (0-based index)
    if current_position <= len(s) and s[current_position - 1] == instruction:
        current_position += 1

print(current_position)