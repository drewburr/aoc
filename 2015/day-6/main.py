from bitarray import bitarray

input_file = "input.txt"
# input_file = "example.txt"

part = 2

class Instruction:
    def __init__(self, action, start, end):
        self.action: str = action
        self.start: list[int] = start
        self.end: list[int] = end


instructions: list[Instruction] = []
grid_size = 1000

if part == 1:
    lights: list[bitarray] = []
    for _ in range(grid_size):
        lights.append(bitarray(grid_size))
else:
    brightLights: list[int] = []
    for _ in range(grid_size):
        brightLights.append([0] * grid_size)


for l in open(input_file):
    l = l.strip().removeprefix('turn ')
    inst = l.split(' ')
    action = inst[0]
    start = list(map(int, inst[1].split(',')))
    end = list(map(int, inst[3].split(',')))

    # print(action, start, end)

    instructions.append(Instruction(action, start, end))

def toggle(start: tuple[int], end: tuple[int]):
    if part == 1:
        # XOR ranges
        for x in range(start[0], end[0]+1):
            strip = lights[x]
            strip[start[1]:end[1]+1] = ~strip[start[1]:end[1]+1]
    else:
        updateBrightness(2, start, end)


def on(start: tuple[int], end: tuple[int]):
    if part == 1:
        # Set ranges high
        for x in range(start[0], end[0]+1):
            lights[x][start[1]:end[1]+1] = 1
    else:
        updateBrightness(1, start, end)

def off(start: tuple[int], end: tuple[int]):
    if part == 1:
        # Set ranges low
        for x in range(start[0], end[0]+1):
            lights[x][start[1]:end[1]+1] = 0
    else:
        updateBrightness(-1, start, end)

def updateBrightness(change, start, end):
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            brightLights[x][y] += change
            if brightLights[x][y] < 0:
                brightLights[x][y] = 0

actions = {
    'toggle': toggle,
    'off': off,
    'on': on
}

for inst in instructions:
    actions[inst.action](inst.start, inst.end)

if part == 1:
    # Sum all high bits
    print(sum(map(
        bitarray.count, lights
    )))
else:
    print(sum(map(sum, brightLights)))
