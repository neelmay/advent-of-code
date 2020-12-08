import os
import re

script_dir = os.path.dirname(__file__)
relative_path = "input.txt"
input_path = os.path.join(script_dir, relative_path)

LINES = list(open(input_path).read().split("\n\n"))
valid_passports = 0

REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def required_fields_present(dictionary):
    return REQUIRED_FIELDS.issubset(dictionary)


for line in LINES:
    key_values = re.split(" |\n", line)
    dictionary = {}
    for key_value in key_values:
        split = key_value.split(":")
        key = split[0]
        value = split[1]

        dictionary[key] = value

    if required_fields_present(dictionary):
        valid_passports += 1

print(valid_passports)
