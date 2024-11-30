from bitarray import bitarray

input_file = "input.txt"

part = 1

class Instruction:
    def __init__(self, action, start, end):
        self.action: str = action
        self.start: list[int] = start
        self.end: list[int] = end


instructions: list[Instruction] = []
lights: list[bitarray] = []

grid_size = 1000

for _ in range(grid_size):
    lights.append(bitarray(grid_size))

for l in open(input_file):
    l = l.strip().removeprefix('turn ')
    inst = l.split(' ')
    action = inst[0]
    start = list(map(int, inst[1].split(',')))
    end = list(map(int, inst[3].split(',')))

    # print(action, start, end)

    instructions.append(Instruction(action, start, end))

def toggle(start: tuple[int], end: tuple[int]):
    # XOR ranges
    for x in range(start[0], end[0]+1):
        strip = lights[x]
        strip[start[1]:end[1]+1] = ~strip[start[1]:end[1]+1]

def on(start: tuple[int], end: tuple[int]):
    # Set ranges high
    for x in range(start[0], end[0]+1):
        lights[x][start[1]:end[1]+1] = 1

def off(start: tuple[int], end: tuple[int]):
    # Set ranges low
    for x in range(start[0], end[0]+1):
        lights[x][start[1]:end[1]+1] = 0

actions = {
    'toggle': toggle,
    'off': off,
    'on': on
}

for inst in instructions:
    actions[inst.action](inst.start, inst.end)

# Sum all high bits
print(sum(map(
    bitarray.count, lights
)))
