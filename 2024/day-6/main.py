input_file = "input.txt"
input_file = "example.txt"

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
loops = 0
spaces = set()

turn_positions = set()

onscreen = True
while onscreen:
    spaces.add(f"{pos[0]},{pos[1]}")

    def get_direction():
        x_dir = direction[0] * (1 if turns % 2 == 0 else 0)
        y_dir = direction[0] * (0 if turns % 2 == 0 else 1)
        return x_dir, y_dir

    def get_facing():
        x_dir, y_dir = get_direction()
        return data[pos[0] + x_dir][pos[1] + y_dir]

    def step():
        global steps, turns
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
            turn_positions.add((pos[0], pos[1], turns % 4))
            direction.append(direction.pop(0))
            print("turn", len(spaces), steps)

        return True

    if onscreen and part == 2:
        # Store state
        _direction = direction.copy()
        _data = data.copy()
        _pos = pos.copy()
        _turns = turns
        _turn_positions = turn_positions.copy()
        _steps = steps
        # Add wall
        x_dir, y_dir = get_direction()
        line = data[pos[0] + x_dir]
        data[pos[0] + x_dir] = line[: pos[1]] + wall + line[pos[1] + 1 :]

        o_turns = turns
        turn_limit = 0
        onscreen = True
        while onscreen and turns - o_turns < 100:
            p_turns = turns
            onscreen = step()
            if p_turns != turns:
                if (pos[0], pos[1], turns % 4) in turn_positions:
                    loops += 1
                    # Reset state
                    direction = _direction
                    data = _data
                    pos = _pos
                    turns = _turns
                    turn_positions = _turn_positions
                    steps = _steps
                    break

    onscreen = step()


print(len(spaces))
print(loops)
