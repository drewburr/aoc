DATA_FILE = 'input.txt'
DAYS = 80
RESET_INDEX = 6
SPAWN_INDEX = 8


def setup():
    data: list[int] = []
    for line in open(DATA_FILE, 'r'):
        # Remove newlines
        l = line.strip()
        fishTimers = line.split(',')
        data = list(map(int, fishTimers))

        # We only want the first line
        return data
    raise Exception('Failed to setup.')

def main():
    timers = [0] * 9

    for t in setup():
        timers[t] += 1

    for _ in range(DAYS):
        spawning = timers.pop(0)
        timers.append(0)

        timers[SPAWN_INDEX] += spawning
        timers[RESET_INDEX] += spawning


    print(sum(timers))


if __name__ == "__main__":
    main()
