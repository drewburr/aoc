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

    tail = (0, 0)
    head = (0, 0)

    positions.add(tail)

    for direction, quantity in movement_data:
        for _ in range(quantity):
            head = move_head(head, *DIRECTION_MAP[direction])

            if distance(head, tail) >= 2:
                # Head is too far away
                new_tail = move_tail(head, tail)
                print(head, tail, "->", new_tail)
                positions.add(new_tail)
                tail = new_tail
            else:
                print(head, tail)

    return len(positions)


def move_head(head: tuple[int, int], x: int, y: int):
    new_head = head[X] + x, head[Y] + y
    return new_head


def move_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
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

    return tuple(new_tail)


def distance(c1: tuple[int, int], c2: tuple[int, int]):
    # √[(x₂ - x₁)² + (y₂ - y₁)²]
    x_dist = c1[X]-c2[X]
    y_dist = c1[Y]-c2[Y]

    tot_dist = pow(pow(x_dist, 2) + pow(y_dist, 2), 1/2)
    return tot_dist


def get_input():
    data: list[tuple[str, int]] = []
    for l in open('input.txt'):
        l = l.replace('\n', '')
        l = l.split(' ')
        data.append((l[0], int(l[1])))

    return data


if __name__ == "__main__":
    answer = main()

    print("Tail positions visited:", answer)
