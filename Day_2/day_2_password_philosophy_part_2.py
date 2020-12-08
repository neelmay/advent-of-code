import os

script_dir = os.path.dirname(__file__)
relative_path = "input.txt"
input_path = os.path.join(script_dir, relative_path)

LINES = list(open(input_path).read().split("\n"))
valid_passwords = 0

for line in LINES:
    exactly_once = False
    index_one = line[: line.index("-")]
    index_two = line[line.find("-") + len("-") : line.find(" ")]

    character = line[line.find(" ") + len(" ") : line.find(":")]

    password = line.rsplit(" ", 1)[1]

    if password[int(index_one) - 1] == character:
        exactly_once = not exactly_once

    if password[int(index_two) - 1] == character:
        exactly_once = not exactly_once

    if exactly_once:
        valid_passwords += 1


print(valid_passwords)
