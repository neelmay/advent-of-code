import os
import math


script_dir = os.path.dirname(__file__)
relative_path = "input.txt"
input_path = os.path.join(script_dir, relative_path)

boarding_passes = list(open(input_path).read().split("\n"))

seat_ids = []

for boarding_pass in boarding_passes:
    # Calculate the ROW
    i = 0
    j = 127
    for char in boarding_pass[0:7]:
        mid = (j - i) / 2

        if char == "F":
            j = math.floor(j - mid)

        if char == "B":
            i = math.ceil(i + mid)

    row = i  # at the end, i and j both would be same which would be the row number

    # Calculate the COL
    m = 0
    n = 7
    for char in boarding_pass[7:10]:
        mid = (n - m) / 2

        if char == "L":
            n = math.floor(n - mid)

        if char == "R":
            m = math.ceil(m + mid)

    col = m  # at the end, m and n both would be same which would be the column number

    seat_ids.append(row * 8 + col)

print("MAX SEAT NUMBER - " + str(max(seat_ids)))

# PART 2
real_sum = sum(seat_ids)
ideal_sum = sum(range(min(seat_ids), max(seat_ids) + 1))

print("MY SEAT NUMBER - " + str(ideal_sum - real_sum))