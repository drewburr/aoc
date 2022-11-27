DATA_FILE = 'input.txt'


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

def calculateCost(positions: list[int], final: int):
    cost = 0
    for p in positions:
        if p >= final:
            cost += p - final
        else:
            cost += final - p

    return cost



def main():
    crabPositions = sorted(setup())
    positions = range(crabPositions[0], crabPositions[-1])

    # for final in range(positions[0], positions[-1]):
    #     cost = calculateCost(positions, final)
    #     print(final, cost, sep=',')

    # bestCostPos = positions[0] - 1
    # bestCost = float('inf')
    # for pos in positions:
    #     if (posCost := calculateCost(crabPositions, pos)) < bestCost:
    #         bestCostPos = pos
    #         bestCost = posCost
    # print(bestCostPos, bestCost)



    # Get the position with the least cost
    while (size := len(positions)) > 1:
        midIndex = size//2
        leftCost = calculateCost(crabPositions, positions[midIndex - 1])
        rightCost = calculateCost(crabPositions, positions[midIndex])
        print(positions)

        print('mid', positions[midIndex - 1], positions[midIndex])

        print(leftCost, rightCost)

        if leftCost < rightCost:
            # Remove all right positions
            if size == 2:
                # Handle if len is 2 and left side wins
                positions = positions[:midIndex + 1]
            else:
                positions = positions[:midIndex]
        else:
            # Remove all left positions
            positions = positions[midIndex:]

    print(positions)

    print(positions[0], calculateCost(crabPositions, positions[0]))


if __name__ == "__main__":
    main()
