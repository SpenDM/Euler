"""Find the sum of all the multiples of 3 or 5 below 1000."""

MAX = 1000

sum = 0

# add multiples of 5
x = 5
while x < MAX:
    sum += x
    x += 5

# add multiples of 3 (except for multiples of 5)
x = 3
while x < MAX:
    if x % 5 != 0:
        sum += x
    x += 3

print(sum)
