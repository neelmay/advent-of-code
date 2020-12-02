import os

script_dir = os.path.dirname(__file__)
RELATIVE_PATH = "input.txt"
input_path = os.path.join(script_dir, RELATIVE_PATH)

# Hashset for O(1) lookup
NUMBERS = set(open(RELATIVE_PATH).read().split())
SUM = 2020


def find_second_number(number):
    diff = SUM - number
    if str(diff) in NUMBERS:
        return diff


for num_1 in NUMBERS:
    num_1 = int(num_1)

    for num_2 in NUMBERS:
        num_2 = int(num_2)
        num_3 = find_second_number(num_1 + num_2)

        if num_3:
            print(num_1)
            print(num_2)
            print(num_3)
            print(num_1 * num_2 * num_3)
            break

    if num_3:
        break
