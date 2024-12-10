input_file = "input.txt"
# input_file = "example.txt"

part = 2

data: list[list[int]] = list()

for l in open(input_file):
    l = l.strip()

    data.append(list([int(x) if x != "." else "." for x in l]))


def move(x, y, i):
    if part == 1:
        found = set()
    else:
        found = list()

    print(x, y)
    if data[x][y] == 9:
        print("found", x, y)
        if part == 1:
            return {(x, y)}
        else:
            return [(x, y)]

    if x - 1 >= 0 and data[x - 1][y] == i + 1:
        f = move(x - 1, y, i + 1)
        if part == 1:
            found.update(f)
        else:
            found += f

    if x + 1 < len(data) and data[x + 1][y] == i + 1:
        f = move(x + 1, y, i + 1)
        if part == 1:
            found.update(f)
        else:
            found += f

    if y - 1 >= 0 and data[x][y - 1] == i + 1:
        f = move(x, y - 1, i + 1)
        if part == 1:
            found.update(f)
        else:
            found += f

    if y + 1 < len(data[0]) and data[x][y + 1] == i + 1:
        f = move(x, y + 1, i + 1)
        if part == 1:
            found.update(f)
        else:
            found += f

    return found


total = 0
for x, l in enumerate(data):
    for y, i in enumerate(l):
        if i == 0:
            total += len(move(x, y, i))


print(total)
