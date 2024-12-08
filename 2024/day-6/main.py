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


def is_loop(x, y, x_dir, y_dir):
    pass


onscreen = True
while True:
    spaces.add(f"{pos[0]},{pos[1]}")

    def get_direction():
        x_dir = direction[0] * (1 if turns % 2 == 0 else 0)
        y_dir = direction[0] * (0 if turns % 2 == 0 else 1)
        return x_dir, y_dir

    def get_facing():
        x_dir, y_dir = get_direction()
        return data[pos[0] + x_dir][pos[1] + y_dir]

    def step():
        try:
            facing = get_facing()
        except Exception as e:
            return False

        print(facing, end=" ")
        print(pos, len(spaces), steps)

        if facing != wall:
            pos[turns % 2] += direction[0]
            steps += 1
        else:
            turns += 1
            direction.append(direction.pop(0))
            print("turn  ", len(spaces), steps)

        return True

    if onscreen and part == 2:
        _turns = turns
        _pos = pos.copy()
        loop_data = data.copy()
        loop_spaces = dict()

        x_dir, y_dir = get_direction()
        id = (2 * x_dir) - y_dir


    onscreen = step()


print(len(spaces))
