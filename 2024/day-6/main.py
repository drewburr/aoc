input_file = "input.txt"
# input_file = "example.txt"

part = 2

data: list[str] = []

processingRules = True
for l in open(input_file):
    l = l.strip()
    data.append(l)

x: int
for i, l in enumerate(data):
    if l.count("^"):
        x = i
        y = l.index("^")
        break


direction = [-1, 1, 1, -1]
pos = [x, y]
turns = 0
wall = "#"
steps = 0
spaces = set()


while (True):
    spaces.add(f'{pos[0]},{pos[1]}')

    x_dir = direction[0] * (1 if turns % 2 == 0 else 0)
    y_dir = direction[0] * (0 if turns % 2 == 0 else 1)
    # print(x_dir, y_dir)

    try:
        facing = data[pos[0]+x_dir][pos[1]+y_dir]
    except Exception as e:
        break

    print(facing, end=' ')
    print(pos, len(spaces), steps)

    if facing != wall:
        pos[turns % 2] += direction[0]
        steps += 1

    else:
        turns += 1
        direction.append(direction.pop(0))
        print('turn  ', len(spaces), steps)

print(len(spaces))
