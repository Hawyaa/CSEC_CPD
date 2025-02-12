import math

y, w = map(int, input().split())
max_val = max(y, w)
favorable = 7 - max_val
gcd_val = math.gcd(favorable, 6)
numerator = favorable // gcd_val
denominator = 6 // gcd_val
print(f"{numerator}/{denominator}")