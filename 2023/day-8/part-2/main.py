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
    currents = list(filter(is_start, data.keys()))
    total = 0
    lengths = [0] * len(currents)
    current_length = [0] * len(currents)
    start_length = [0] * len(currents)

    while True:
        for step in steps:
            total += 1

            for i, current in enumerate(currents):
                currents[i] = data[current][step]
                current_length[i] += 1

                if not is_in_progress(currents[i]):
                    lengths[i] = current_length[i]

                    if not start_length[i]:
                        start_length[i] = current_length[i]

                    current_length[i] = 0

            if not 0 in start_length:
                return start_length

            in_progress = list(filter(is_in_progress, currents))
            if not in_progress:
                return total

            if len(in_progress) < (len(currents)):
                print('start', start_length)
                print('end  ', lengths)
                print(currents, len(currents) - len(in_progress), total)
                # return
            # else:
            #     print(currents)

def find_factors(x: int):
    i = 2
    factors = list()
    while x > i:
        while x % i == 0:
            factors.append(i)
            x = x // i

        i += 1

    factors.append(x)
    return factors

def main():
    steps, data = parse_input()

    distances = traverse(steps, data)

    distance_factors = [find_factors(d) for d in distances]

    distance_factors = set([i for l in distance_factors for i in l])

    lcm = 1
    for i in distance_factors:
        lcm *= i

    print(distance_factors)
    print(lcm)



14,265,111,103,729

if __name__ == "__main__":
    main()
