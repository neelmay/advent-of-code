import os

script_dir = os.path.dirname(__file__)
relative_path = "input.txt"
input_path = os.path.join(script_dir, relative_path)

# Hashset for O(1) lookup
NUMBERS = set(open(input_path).read().split())
SUM = 2020


def find_second_number(number):
    diff = SUM - number
    if str(diff) in NUMBERS:
        return diff


for num in NUMBERS:
    num_1 = int(num)
    num_2 = find_second_number(num_1)

    if num_2:
        print(num_1)
        print(num_2)
        print(num_1 * num_2)
        break
