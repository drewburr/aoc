input_file = "input.txt"
# input_file = "example.txt"

part = 2

data: list[list[str]] = []
letters = "XMAS"

sample: list[list[str]] = []

for l in open(input_file):
    l = l.strip()
    data.append(list(l))


# def crawl(x, y, letter_i=1):
#     found = 0
#     next = letters[letter_i]

#     x_range = range(-1 if x != 0 else 0, 1 if x != len(data[0]) - 1 else 0)
#     y_range = range(-1 if y != 0 else 0, 1 if y != len(data) - 1 else 0)
#     print(x_range, y_range)

#     for x_offset in x_range:
#         for y_offset in y_range:
#             if data[y + y_offset][x + x_offset] == next:
#                 print("Found", letters[letter_i], "at offset", x_offset, y_offset)
#                 if letters[letter_i + 1] == letters[-1]:
#                     found += 1
#                 else:
#                     found += crawl(x + x_offset, y + y_offset, letter_i + 1)

#     return found

def check_direction(x, y, x_offset, y_offset, letter_i=0):
    next = letters[letter_i + 1]

    if x + x_offset < 0 or x + x_offset > len(data) - 1:
        return 0
    if y + y_offset < 0 or y + y_offset > len(data[0]) - 1:
        return 0

    print(
        "from",
        data[x][y],
        "searching for",
        next,
        f"({data[x + x_offset][y + y_offset]})",
    )
    if data[x + x_offset][y + y_offset] == next:
        if next == letters[-1]:
            print("Match found!", x + x_offset, y + y_offset)
            return 1
        return check_direction(
            x + x_offset, y + y_offset, x_offset, y_offset, letter_i + 1
        )

    return 0


def search(x, y):
    found = 0
    next = letters[1]

    x_range = list(range(-1 if x != 0 else 0, 2 if x != len(data[0]) - 1 else 1))
    y_range = list(range(-1 if y != 0 else 0, 2 if y != len(data) - 1 else 1))

    print(x_range, y_range)

    for x_offset in x_range:
        for y_offset in y_range:
            if data[x + x_offset][y + y_offset] == next:
                print("checking direction", x_offset, y_offset)
                found += check_direction(x, y, x_offset, y_offset)

    return found


def check_mas(x, y):
    """ x,y are the cordinates of the 'a' in the X-MAS"""
    tlc = data[x-1][y-1]
    blc = data[x+1][y-1]
    trc = data[x-1][y+1]
    brc = data[x+1][y+1]

    if x - 1 < 0 or y - 1 < 0:
        return 0
    if x + 1 > len(data) -1 or y+1 > len(data[0]):
        return 0

    if tlc == 'M' and brc == 'S' or tlc == 'S' and brc == 'M':
        if trc == 'M' and blc == 'S' or trc == 'S' and blc == 'M':
            # print(x,y)
            print(''.join(data[x-1][y-1:y+2]))
            print(''.join(data[x][y-1:y+2]))
            print(''.join(data[x+1][y-1:y+2]))
            print(1, '@', x, y)
            print()
            return 1
    return 0

total = 0

for x, line in enumerate(data):
    for y, char in enumerate(line):
        if part == 1:
            if char == letters[0]:
                print("Start", letters[0], "at", x, y)
                total += search(x, y)
        if part == 2:
            if char == 'A':
                try:
                    total += check_mas(x,y)
                    # print(found)
                    # print()
                except:
                    pass

print(total)

# high: 1886
# high: 1881
