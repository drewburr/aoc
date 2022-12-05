import string

data: list[tuple[str, str]] = []
buffer: list[str] = []

# String containing the entire alphabet
alphabet=string.ascii_lowercase+string.ascii_uppercase

for l in open('input.txt'):
    l = l.strip()

    buffer.append(l)

    # Append in groups of 3
    if len(buffer) == 3:
        data.append(tuple(buffer))
        buffer = []

total = 0

for s1, s2, s3 in data:
    print(s1, s2, s3)
    val = 0
    for x in s1:
        if s2.find(x) != -1 and s3.find(x) != -1:
            print('Found item:', x)
            val = alphabet.find(x) + 1
            break
    if not val:
        raise Exception('No duplicate item found!')

    total += val

print(total)
