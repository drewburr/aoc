import re
from re import Match

input_file = 'example.txt'

data: list[str] = []
total = 0


def is_symbol_adjacent(start, end, line):
    frame = ''
    symbol_re = re.compile(r'[^0-9.]')
    width = end - start

    # print('pre-width',start,end)

    if start > 0:
        start -= 1

    # if end > len(data[line])-1:
    #     end -= 1

    print('width',start,end)

    # Top
    if line > 0:
        frame += data[line-1][start:end]
        print(data[line-1][start:end])

    # Middle-ends
    frame += data[line][start]
    frame += data[line][end]
    print(data[line][start], data[line][end])
    # print(data[line][start:end])


    # print('ends', data[line][start], data[line][end])

    # Bottom
    if line < len(data)-1:
        frame += data[line+1][start:end]
        print(data[line+1][start:end])

    # print(frame)

    return bool(symbol_re.search(frame))

for l in open(input_file):
    data.append(l.strip())


number_re = re.compile(r'([0-9]+)')
for line_i, d in enumerate(data):
    print('line', line_i)
    match: Match
    while match := number_re.search(d):
        start_i, end_i = match.span()
        # print(match)
        print(match.groups()[0])
        # Remove match
        d = ('.' * end_i) + d[end_i:]
        print(is_symbol_adjacent(start_i, end_i, line_i))
        print('')


    # print(res)


#     re.findall()
#     card, nums = l.split(':')

#     # Convert values into sets
#     selected, winning = [set(x.strip().split()) for x in nums.split('|')]

# data.append((card, selected, winning))
