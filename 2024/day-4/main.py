import re

input_file = "input.txt"
# input_file = "example.txt"

part = 2

data: list[list[str]] = []

for l in open(input_file):
    l = l.strip()
    data.append(l)
