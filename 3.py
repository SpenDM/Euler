"""What is the largest prime factor of the number 600851475143 ?"""

TARGET_1 = 13195
TARGET_2 = 600851475143

target = TARGET_2
factors = []
x = 1
while x <= target:
    if target % x == 0:
        factors.append(x)
        target = target / x
    x += 1
print("Prime factors: " + ",".join([str(n) for n in factors]))
