data = []
total = 0

crates_finished = False
crate_lines = []
crate_stacks = []
movements = 0

for l in open('input.txt'):
    l = l.replace('\n', '')

    if l:
        if not crates_finished:
            crate_line = l[1::4]
            if not crate_line[0] == '1':
                # Crate data
                crate_lines.append(list(crate_line))
            else:
                for _ in range(len(crate_line)):
                    crate_stacks.append(list())

                # Parse and format
                crate_lines.reverse()

                for line in crate_lines:
                    for i, crate in enumerate(line):
                        if crate != ' ':
                            crate_stacks[i].append(crate)
        else:
            move_data = l.split(' ')
            quantity = int(move_data[1])
            origin = int(move_data[3])
            destination = int(move_data[5])

            movements += quantity

            # Move 'dem crates
            length = len(crate_stacks[origin - 1])
            for _ in range(quantity):
                move_crate=crate_stacks[origin - 1].pop(length-quantity)
                crate_stacks[destination - 1].append(move_crate)
    else:
        crates_finished = True


print(crate_stacks)

answer = ''

for stack in crate_stacks:
    answer += stack[-1]


print(answer)

print('moves:', movements)
