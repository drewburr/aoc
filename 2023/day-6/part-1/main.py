input_file = "input.txt"

import math

def parse_input():
    def parse_values(s: str):
        d = s.split(":")[1].strip().split()
        return [int(x) for x in d]

    with open(input_file) as f:
        times = parse_values(f.readline())
        distances = parse_values(f.readline())

    return zip(times, distances)


def calculate_intersections(t, d):
    """Returns left and right of the winnable x-value range"""



    res1 = (t + (t**2 - 4 * d) ** 0.5) / 2
    res2 = (t - (t**2 - 4 * d) ** 0.5) / 2


    if res1 > res2:
        res1, res2 = res2, res1

    # Compensate for range issues
    if res2 % 1 == 0:
        res2 -= 1

    return math.floor(res1), math.floor(res2)


def main():
    data = parse_input()

    total = 1

    for d in data:
        r1, r2 = calculate_intersections(*d)
        print(r1, r2)
        print(r2-r1)
        total *= r2-r1

    print(total)


if __name__ == "__main__":
    main()
