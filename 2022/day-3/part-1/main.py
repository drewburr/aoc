import string

data = []

# String containing the entire alphabet
alphabet=string.ascii_lowercase+string.ascii_uppercase

for l in open('input.txt'):
    l = l.strip()

    c1 = l[:len(l)//2]
    c2 = l[len(l)//2:]

    data.append((c1, c2))

total = 0

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

print(total)
