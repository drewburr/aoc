DATA_FILE = 'input.txt'
# COUNT_VALS = [1, 4, 7, 8]
COUNT_LENGTHS = [2,4,3,7]

def setup():
    data: list[str] = []
    for line in open(DATA_FILE, 'r'):
        if line:
            print(line)
            outputValues = line.split('|')[1].strip()
            data.append(outputValues)

    return data
    # raise Exception('Failed to setup.')


def main():
    data = setup()

    total = 0

    for d in data:
        values = d.split(' ')
        for v in values:
            if len(v) in COUNT_LENGTHS:
                print(v)
                total += 1

    print(total)


if __name__ == "__main__":
    main()
