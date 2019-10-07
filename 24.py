import math

MAX = 1000000


def top_level_get_permutations(x, num_of_different_first_digits):
    permutations = []

    end = len(x) if len(x) < num_of_different_first_digits else num_of_different_first_digits

    for i in range(end):
        x_without_i = [j for j in x if j != i]
        sub_permutations = get_permutations(x_without_i)

        i_permutations = []
        for s in sub_permutations:
            s = [i] + s
            i_permutations.append(s)

        for p in i_permutations:
            permutations.append(p)

    # print(permutations)
    return permutations[MAX - 1]


def get_permutations(x):
    permutations = []
    if len(x) == 1:
        permutations = [x]
    else:
        for i in x:
            x_without_i = [j for j in x if j != i]
            sub_permutations = get_permutations(x_without_i)

            i_permutations = []
            for s in sub_permutations:
                s = [i] + s
                i_permutations.append(s)

            for p in i_permutations:
                permutations.append(p)

    return permutations


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


sum = 0
permuts_per_first_digit = math.factorial(len(x) - 1)
num_of_different_first_digits = math.ceil(float(MAX) / float(permuts_per_first_digit))

all_permutations = top_level_get_permutations(x, num_of_different_first_digits)
print(all_permutations)