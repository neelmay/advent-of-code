import os

script_dir = os.path.dirname(__file__)
relative_path = "input.txt"
input_path = os.path.join(script_dir, relative_path)

GROUPS = list(open(input_path).read().split("\n\n"))

# PART 1
unique_sum = 0
for group in GROUPS:
    group = group.replace("\n", "")

    unique_chars = len(set(group))

    unique_sum += unique_chars

print("Some of UNIQUE characters in a group - " + str(unique_sum))


# PART 2
common_sum = 0
for group in GROUPS:
    individuals = group.split("\n")

    sets = [set(x) for x in individuals]
    common_chars = set.intersection(*sets)

    common_sum += len(common_chars)

print("Some of COMMON characters in a group - " + str(common_sum))