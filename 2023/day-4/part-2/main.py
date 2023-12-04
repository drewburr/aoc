input_file = 'input.txt'

data = []
total = 0
copies_i = 3

for l in open(input_file):
    l = l.strip()
    card, nums = l.split(':')

    # Convert values into sets
    selected, winning = [set(x.strip().split()) for x in nums.split('|')]

    data.append([card, selected, winning, 1])

for card_i, (card, selected, winning, copies) in enumerate(data):
    matches = 0

    for v in winning:
        x = len(selected)
        selected.add(v)
        if len(selected) == x:
            matches += 1

    if matches > 0:
        # Create copies of downstream cards
        for offset in range(matches):
            update_i = card_i + offset + 1
            # Prevent OOR
            if update_i < len(data):
                data[update_i][copies_i] += copies

    print(card, copies)
    total += copies

print(total)
