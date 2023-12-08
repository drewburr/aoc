input_file = "input.txt"

import re


def parse_input():
    steps: tuple[str] = None
    data = {}

    for l in open(input_file):
        l = l.strip()
        if not l:
            continue

        if not steps:
            t = lambda x: 0 if x == "L" else 1
            steps = [t(x) for x in l]
            steps = tuple(steps)
            continue

        d: list[str] = re.findall(r"[A-Z0-9]{3}", l)
        name = d[0]
        paths = (d[1], d[2])
        data[name] = paths

    return steps, data


def traverse(steps: tuple[str], data: dict):
    is_start = lambda x: x[2] == 'A'
    is_in_progress = lambda x: x[2] != 'Z'
    currents = filter(is_start, data.keys())
    total = 0

    while True:
        for step in steps:
            total += 1
            currents = [data[current][step] for current in currents]
            in_progress = list(filter(is_in_progress, currents))
            if not in_progress:
                return total

def main():
    steps, data = parse_input()

    total = traverse(steps, data)
    print(total)


if __name__ == "__main__":
    main()
