import string

data = []
alphabet=string.ascii_letters

# Get and format input data
for l in open('input.txt'):
    l = l.strip()

    c1 = l[:len(l)//2]
    c2 = l[len(l)//2:]

    data.append((c1, c2))

total = 0

# Check for cross-compartment duplicates
for c1, c2 in data:
    print(c1, c2)
    val = 0
    for x in c1:
        if c2.find(x) != -1:
            print('Found item:', x)
            val = alphabet.find(x) + 1
            break
    if not val:
        raise Exception('No duplicate item found!')

    total += val

# Print answer
print(total)
