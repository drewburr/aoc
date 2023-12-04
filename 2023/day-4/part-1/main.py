input_file = 'input.txt'

data = []
points = 0

for l in open(input_file):
    l = l.strip()
    card, nums = l.split(':')

    # Convert values into sets
    selected, winning = [set(x.strip().split()) for x in nums.split('|')]

    data.append((card, selected, winning))

for card, selected, winning in data:
    matches = 0

    for v in winning:
        x = len(selected)
        selected.add(v)
        if len(selected) == x:
            matches += 1

    if matches > 0:
        value = 2 ** (matches - 1)
        # print(card, 'matches:', matches, 'earning', value)
        points += value

print(points)
