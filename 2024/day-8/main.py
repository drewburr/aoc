input_file = "input.txt"
# input_file = "example.txt"

from operator import add, sub

part = 2

data: list[str] = []

for l in open(input_file):
    l = l.strip()
    data.append(l)


x_max = len(data) - 1
y_max = len(data[0]) - 1
total = 0

frequencies: dict[str, list[tuple[int, int]]] = dict()
nodes: set[tuple[int, int]] = set()

for x, line in enumerate(data):
    for y, c in enumerate(line):
        if c != ".":
            if not frequencies.get(c):
                frequencies[c] = list()
            frequencies[c].append((x, y))

def in_bounds(cords: tuple[int, int]):
    x = cords[0]
    y = cords[1]
    return not (x > x_max or x < 0 or y > y_max or y < 0)

def get_antinodes(cords: tuple, dist):
    nodes = set()
    for op in (add, sub):
        anti_cords = tuple(map(op, cords, dist))
        if anti_cords == f_cords:
            anti_cords = tuple(map(op, anti_cords, dist))
        if in_bounds(anti_cords) and anti_cords not in nodes:
            # print(f'{cords} <-> {f_cords}: {anti_cords}')
            # print(anti_cords)
            nodes.add(anti_cords)

    return nodes


def get_resonant(cords: tuple, dist):
    nodes = set()
    t_cords = tuple(cords)
    for op in (add, sub):
        while in_bounds(t_cords):
            nodes.add(t_cords)
            t_cords = tuple(map(op, t_cords, dist))

    return nodes

for freq, freq_list in frequencies.items():
    # print(f'Checking for antinodes in freq: {freq}')
    for cords in freq_list:
        for f_cords in frequencies[freq]:
            if cords == f_cords:
                continue

            dist = tuple(map(sub, f_cords, cords))

            if part == 1:
                nodes.update(get_antinodes(cords, dist))
            else:
                nodes.update(get_resonant(cords, dist))

# print(nodes)
print(len(nodes))
