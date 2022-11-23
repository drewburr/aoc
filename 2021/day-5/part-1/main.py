DATA_FILE = 'input.txt'
DATA_SIZE = 1000


def setup():
    data: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for line in open(DATA_FILE, 'r'):
        # Remove newlines
        l = line.strip()
        points = l.split(' -> ')
        start = tuple(map(int, points[0].split(',')))
        end = tuple(map(int, points[1].split(',')))

        #((x, y), (x, y))
        data.append((start, end))

    return data


def generate_grid(data: list[tuple[tuple[int, int], tuple[int, int]]]):
    grid = []
    for _ in range(DATA_SIZE):
        grid.append([0]*DATA_SIZE)

    def plot(x1, y1, x2, y2):
        x_offset = 1 if x1 <= x2 else -1
        y_offset = 1 if y1 <= y2 else -1

        for x in range(x1, x2+x_offset, x_offset):
            for y in range(y1, y2+y_offset, y_offset):
                grid[x][y] += 1

    for (x1, y1), (x2, y2) in data:
        if x1 == x2 or y1 == y2:
            plot(x1, y1, x2, y2)

    return grid


def main():
    data = setup()
    grid = generate_grid(data)

    # for l in zip(*grid):
    #     print(l)

    total_points = 0

    for l in grid:
        res = filter(lambda x: x > 1, l)
        total_points += len(list(res))

    print(total_points)


if __name__ == "__main__":
    main()
