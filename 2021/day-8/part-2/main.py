DATA_FILE = 'input.txt'
# COUNT_VALS = [1, 4, 7, 8]
COUNT_LENGTHS = [2, 4, 3, 7]

TOP = 'a'
TOP_LEFT = 'b'
TOP_RIGHT = 'c'
MIDDLE = 'd'
BOTTOM_LEFT = 'e'
BOTTOM_RIGHT = 'f'
BOTTOM = 'g'

SEGMENT_MAP = {
    '0': ['a', 'b', 'c', 'e', 'f', 'g'],
    '1': ['c', 'f'],
    '2': ['a', 'c', 'd', 'e', 'g'],
    '3': ['a', 'c', 'd', 'f', 'g'],
    '4': ['b', 'c', 'd', 'f'],
    '5': ['a', 'b', 'd', 'f', 'g'],
    '6': ['a', 'b', 'd', 'e', 'f', 'g'],
    '7': ['a', 'c', 'f'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'f', 'g']
}


def setup():
    data: list[str] = []
    for line in open(DATA_FILE, 'r'):
        if line:
            outputValues = list(map(str.strip, line.split('|')))
            data.append(outputValues)

    return data
    # raise Exception('Failed to setup.')


def dedup(src: list[str], dest: list[str]):
    """
    Values in src will be removed from dest
    """
    dedup: list[str] = []
    for s in dest:
        if s not in src:
            dedup.append(s)

    return dedup


def segmentMatches(seg1: list[str], seg2: list[str]):
    """
    Counts the number of common segments
    """
    matches = 0
    for seg in seg1:
        if seg in seg2:
            matches += 1
    return matches


def decode(signalStr: str):
    code: dict[str, str] = {}
    signals: dict[int, list[list[str]]] = {}

    # Store signals based on length
    for s in signalStr.split(' '):
        length = len(s)
        if not signals.get(length):
            signals[length] = []

        signals[length].append(s)

    # Extract known values
    one = signals[2][0]
    four = signals[4][0]
    seven = signals[3][0]
    eight = signals[7][0]

    # Setup 5 segment values
    two = None
    three = None
    five = None

    # Setup 6 segment values
    zero = None

    # Top segment found
    seven = dedup(one, seven)
    code[seven[0]] = TOP

    # Identify two, three, and five
    for signal in signals[5]:
        uniqFour = dedup(one, four)
        oneMatches = segmentMatches(one, signal)
        fourMatches = segmentMatches(uniqFour, signal)

        if oneMatches == 2:
            # Three shares all segments with one
            three = signal
        elif fourMatches == 2:
            # Five shares unique segments with four
            five = signal
        else:
            # Two is the only value left
            two = signal

    invertedOne = dedup(one, eight)
    tr = dedup(invertedOne, two)[0]
    br = dedup(invertedOne, five)[0]

    code[tr] = TOP_RIGHT
    code[br] = BOTTOM_RIGHT

    tl = dedup(three, five)[0]
    bl = dedup(three, two)[0]

    code[tl] = TOP_LEFT
    code[bl] = BOTTOM_LEFT

    # Identify zero
    for signal in signals[6]:
        matches = segmentMatches([tr, bl], signal)

        if matches == 2:
            zero = signal

    mid = dedup(zero, eight)[0]
    code[mid] = MIDDLE

    bot = dedup(code.keys(), eight)[0]
    code[bot] = BOTTOM

    return code


def translate(code: dict[str, str], values: str):
    vals = values.split(' ')
    t_vals: list[list[str]] = []

    for v in vals:
        t_val: list[str] = []
        for c in v:
            # Translate character using code map
            t_val.append(code[c])
        t_vals.append(t_val)

    return t_vals

def compute(segments: list[list[str]]):
    def getValue(seg: list[str]):
        s_seg = sorted(seg)
        for v, chars in SEGMENT_MAP.items():
            # print(seg)
            if s_seg == chars:
                return v

    result = list(map(getValue, segments))
    value = ''.join(result)
    return int(value)



def main():
    data = setup()

    total = 0

    for signal, out in data:
        code = decode(signal)
        translated = translate(code, out)
        total += compute(translated)

    print(total)


if __name__ == "__main__":
    main()
