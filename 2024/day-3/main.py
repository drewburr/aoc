import re

input_file = "input.txt"
# input_file = "example.txt"

part = 2

regex = re.compile(r"(mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\))")

with open(input_file) as f:
    l = f.read().strip()


matches = re.findall(regex, l)
total = 0
do = True

for m in matches:
    if m[:5] == "don't" and part == 2:
        do = False
    elif m[:2] == "do" and part == 2:
        do = True
    elif do:
        split = m.split(",")
        left = split[0].split("(")[1]
        right = split[1].split(")")[0]

        total += int(left) * int(right)

print(total)
