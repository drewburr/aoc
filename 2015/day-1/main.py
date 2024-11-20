input_file = 'input.txt'

part = 2

data = []

with open(input_file, 'r') as f:
    input = f.read()

floor = 0
moves = 0

for c in input:
    moves += 1
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
        if part == 2 and floor < 0:
            break

if part == 1:
    print(floor)
else:
    print(moves)
