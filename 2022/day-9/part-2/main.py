total = 0

X = 0
Y = 1

DIRECTION_MAP = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}


def main():
    movement_data = get_input()
    positions = set()

    snake: list[list[int]] = list()
    head = [0, 0]

    for _ in range(9):
        snake.append([0,0])

    positions.add(tuple(snake[-1]))

    for direction, quantity in movement_data:
        for _ in range(quantity):
            head = move_head(head, *DIRECTION_MAP[direction])

            h = head
            new_snake = list()
            for t in snake:
                if distance(h, t) >= 2:
                    # Head is too far away
                    new_t = move_tail(h, t)
                    print(h, t, "->", new_t)
                    t = new_t
                else:
                    print(h, t)
                    pass

                new_snake.append(t)
                h = t  # Adjust head for the next loop

            snake = new_snake
            positions.add(tuple(snake[-1]))
            display(head,snake)
            print()

        # break

    return len(positions)


def move_head(head: list[int], x: int, y: int):
    new_head = [head[X] + x, head[Y] + y]
    return new_head


def move_tail(head: list[int], tail: list[int]) -> list[int]:
    new_tail = list(tail)
    x_offset = 1 if head[X] > tail[X] else -1
    y_offset = 1 if head[Y] > tail[Y] else -1

    if head[X] == tail[X]:
        new_tail[Y] += y_offset
    elif head[Y] == tail[Y]:
        new_tail[X] += x_offset
    else:
        new_tail[X] += x_offset
        new_tail[Y] += y_offset

    return new_tail


def distance(c1: list[int], c2: list[int]):
    # √[(x₂ - x₁)² + (y₂ - y₁)²]
    x_dist = c1[X]-c2[X]
    y_dist = c1[Y]-c2[Y]

    tot_dist = pow(pow(x_dist, 2) + pow(y_dist, 2), 1/2)
    return tot_dist


def get_input():
    data: list[list[str, int]] = []
    for l in open('input.txt'):
        l = l.replace('\n', '')
        l = l.split(' ')
        data.append((l[0], int(l[1])))

    return data


def display(head: list[int], snake: list[list[int]]):
    return
    all = [head] + snake

    grid = []
    size = 31
    offset = size//2

    for y in range(size):
        row = []
        for x in range(size):
            row.append('.')
        grid.append(row)

    for i, (x, y) in enumerate(all):
        grid[y+offset][x+offset] = str(i)

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    answer = main()

    print("Tail positions visited:", answer)


# low = 2492
