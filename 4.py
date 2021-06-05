# Find the largest palindromic number that is the product of two 3-digit numbers

import math

MAX = 999
MIN = 100


def main():

    largest = 0
    larger_result_factor = 0
    smaller_result_factor = 0

    larger_factor = MAX
    while larger_factor >= MIN:

        # Stop processing if reach a factor that's been used for a product
        if larger_factor <= smaller_result_factor:
            break

        # Don't repeat combos tried before, second factor is always the smaller one
        smaller_factor = larger_factor
        while smaller_factor >= MIN:

            product = larger_factor * smaller_factor

            if is_palindrome(product) and product > largest:
                largest = product
                larger_result_factor = larger_factor
                smaller_result_factor = smaller_factor
                break

            smaller_factor -= 1

        larger_factor -= 1

    # Report result
    print("Largest palindrome: " + str(largest))
    print(str(larger_result_factor) + " * " + str(smaller_result_factor))


def is_palindrome(num):
    palindrome = True

    num_string = str(num)
    half = int(math.ceil(len(num_string)/2) - 1)

    for i in range(half+1):
        if num_string[i] != num_string[-(i+1)]:
            palindrome = False

    return palindrome


if __name__ == '__main__':
    main()
