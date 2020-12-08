import os

script_dir = os.path.dirname(__file__)
relative_path = "input.txt"
input_path = os.path.join(script_dir, relative_path)

LINES = list(open(input_path).read().split("\n"))
valid_passwords = 0

for line in LINES:
    minimum = line[: line.index("-")]
    maximum = line[line.find("-") + len("-") : line.find(" ")]

    character = line[line.find(" ") + len(" ") : line.find(":")]

    password = line.rsplit(" ", 1)[1]
    character_count = password.count(character)

    if character_count >= int(minimum) and character_count <= int(maximum):
        valid_passwords += 1


print(valid_passwords)
