def main():
    register_x = 1
    cycle_count = 0
    operation_count = 0
    signal_sum = 0

    for l in open('input.txt'):
        l = l.replace('\n', '')
        l = l.split(' ')
        operation = l[0]
        addx = 0

        if operation == 'noop':
            cycles = 1
        elif operation == 'addx':
            cycles = 2

        for i in range(cycles):
            cycle_count += 1

            if register_x and i == 1:
                register_x += int(l[1])

            if (cycle_count - 20) % 40 == 0:
                # print(cycle_count)
                signal = register_x * cycle_count
                signal_sum += signal
                print(cycle_count, register_x, signal)

    print(signal_sum)


if __name__ == "__main__":
    main()
