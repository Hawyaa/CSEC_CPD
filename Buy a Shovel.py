k, r = map(int, input().split())
count = 1  # Start with 1 shovel

while True:
    total_cost = k * count
    remainder = total_cost % 10
    if remainder == 0 or remainder == r:
        print(count)
        break
    count += 1