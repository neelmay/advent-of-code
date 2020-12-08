import os
import re

script_dir = os.path.dirname(__file__)
relative_path = "input.txt"
input_path = os.path.join(script_dir, relative_path)

LINES = list(open(input_path).read().split("\n\n"))

BIRTH_YEAR = "byr"
ISSUE_YEAR = "iyr"
EXPIRATION_YEAR = "eyr"
HEIGHT = "hgt"
HAIR_COLOR = "hcl"
EYE_COLOR = "ecl"
PASSPORT_ID = "pid"

REQUIRED_FIELDS = {
    BIRTH_YEAR,
    ISSUE_YEAR,
    EXPIRATION_YEAR,
    HEIGHT,
    HAIR_COLOR,
    EYE_COLOR,
    PASSPORT_ID,
}

valid_passports = 0


def required_fields_present(dictionary):
    return REQUIRED_FIELDS.issubset(dictionary)


def birth_year_valid(birth_year):
    return 1920 <= int(birth_year) <= 2002


def issue_year_valid(issue_year):
    return 2010 <= int(issue_year) <= 2020


def expiration_year_valid(expiration_year):
    return 2020 <= int(expiration_year) <= 2030


def height_valid(height):
    if height.endswith("cm"):
        number = height.strip("cm")
        return 150 <= int(number) <= 193

    if height.endswith("in"):
        number = height.strip("in")
        return 59 <= int(number) <= 76

    return False


def hair_color_valid(hair_color):
    pattern = re.compile("[a-f0-9]+")
    color_code = hair_color[1:]
    return (
        hair_color[0] == "#" and len(color_code) == 6 and pattern.fullmatch(color_code)
    )


def eye_color_valid(eye_color):
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return eye_color in valid_eye_colors


def passport_id_valid(passport_id):
    return len(passport_id) == 9 and passport_id.isdigit()


for line in LINES:
    key_values = re.split(" |\n", line)
    dictionary = {}
    for key_value in key_values:
        split = key_value.split(":")
        key = split[0]
        value = split[1]

        dictionary[key] = value

    if (
        required_fields_present(dictionary)
        and birth_year_valid(dictionary[BIRTH_YEAR])
        and issue_year_valid(dictionary[ISSUE_YEAR])
        and expiration_year_valid(dictionary[EXPIRATION_YEAR])
        and height_valid(dictionary[HEIGHT])
        and hair_color_valid(dictionary[HAIR_COLOR])
        and eye_color_valid(dictionary[EYE_COLOR])
        and passport_id_valid(dictionary[PASSPORT_ID])
    ):
        valid_passports += 1

    print(dictionary)

print(valid_passports)
