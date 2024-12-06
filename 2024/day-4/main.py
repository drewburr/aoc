input_file = "input.txt"
input_file = "example.txt"

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

def search(x, y, direction: tuple[int, int], letter_i=1):
    found = 0
    next = letters[letter_i]
    x_offset, y_offset = direction

    if data[y + y_offset][x + x_offset] == next:
        if letters[letter_i + 1] == letters[-1]:
            return 1
        else:
            return search(x + x_offset, y + y_offset, direction, letter_i + 1)

    return 0

total = 0

for x, line in enumerate(data):
    for y, char in enumerate(line):

        if char == letters[0]:
            print("Start", letters[0], "at", x, y)
            total += search(x, y)


print(total)
