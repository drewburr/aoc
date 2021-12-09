#!/bin/python3

last_val = None
positive_deltas = 0

for line in open('input.txt', 'r'):
    val = int(line)
    if last_val is not None:
        if val > last_val:
            ## The depth has incremented
            positive_deltas += 1

    last_val = val

print(positive_deltas)
