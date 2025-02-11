s = input().strip()
current = 0  # Starting at 'a' which is position 0
total_rotations = 0

for char in s:
    next_pos = ord(char) - ord('a')
    # Calculate the minimal steps between current and next position
    diff = abs(current - next_pos)
    minimal_steps = min(diff, 26 - diff)
    total_rotations += minimal_steps
    current = next_pos  # Update current position to the next character

print(total_rotations)