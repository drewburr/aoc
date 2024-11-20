input_file = "input.txt"

part = 2
data = []

with open(input_file, "r") as f:
    input = f.read().strip()


grid: dict[int, dict[int, int]]
grid = dict()

cords = [[0, 0], [0, 0]]
turn = 0


def deliver(x, y):
    if not grid.get(x):
        grid[x] = dict()

    if not grid[x].get(y):
        grid[x][y] = 0

    grid[x][y] += 1


cord = cords[turn % 2]
deliver(*cord)

for c in input:
    if part == 2:
        turn += 1

    cord = cords[turn % 2]
    if c == "<":
        cord[0] += -1
    elif c == ">":
        cord[0] += 1
    elif c == "^":
        cord[1] += 1
    elif c == "v":
        cord[1] += -1

    deliver(*cord)


def count_houses(grid):
    ht = 0
    for x_res in grid.values():
        for _ in x_res.values():
            ht += 1
    return ht


total = 0
total = count_houses(grid)
print(total)
