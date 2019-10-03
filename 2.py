"""By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms."""

MAX = 4000000

sum = 0
first = 1
second = 2

while second < MAX:
    if second % 2 == 0:
        sum += second

    next = first + second
    first = second
    second = next

print(sum)
