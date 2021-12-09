#!/bin/python3

window = list()
last_sum = None
positive_deltas = 0

for line in open('input.txt', 'r'):
    depth = int(line)

    window.append(depth)

    if len(window) == 3:
        # Add the current window, then compare
        this_sum = sum(window)

        if last_sum is not None and this_sum > last_sum:
            positive_deltas += 1

        window.pop(0)
        last_sum = this_sum

print(positive_deltas)
