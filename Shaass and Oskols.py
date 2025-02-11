n = int(input())
wires = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    xi, yi = map(int, input().split())
    wire_index = xi - 1  # Convert to 0-based index
    current_birds = wires[wire_index]
    
    left_birds = yi - 1
    right_birds = current_birds - yi
    
    # Reset current wire's birds to 0
    wires[wire_index] = 0
    
    # Distribute left birds to the upper wire if it exists
    upper_wire = wire_index - 1
    if upper_wire >= 0:
        wires[upper_wire] += left_birds
    
    # Distribute right birds to the lower wire if it exists
    lower_wire = wire_index + 1
    if lower_wire < n:
        wires[lower_wire] += right_birds

# Print the result for each wire
for birds in wires:
    print(birds)