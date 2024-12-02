def main():
    register_x = 1
    cycle_count = 0
    signal_sum = 0

    line = []

    for l in open('input.txt'):
        l = l.replace('\n', '')
        l = l.split(' ')
        operation = l[0]
        addx = 0

        if operation == 'noop':
            cycles = 1
        elif operation == 'addx':
            cycles = 2
            addx = int(l[1])

        for i in range(cycles):
            if abs(cycle_count % 40 - register_x) <= 1:
                line.append('#')
            else:
                line.append(' ')

            cycle_count += 1

            if (cycle_count - 20) % 40 == 0:
                signal = register_x * cycle_count
                signal_sum += signal

            if len(line) == 40:
                print_line(line)
                line = []

            if addx and i == 1:
                register_x += addx

    print(signal_sum)


def print_line(line):
    print(''.join(line))


if __name__ == "__main__":
    main()
