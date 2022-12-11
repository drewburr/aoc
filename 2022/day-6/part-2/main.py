data = []
total = 0


for l in open('input.txt'):
    l = l.replace('\n', '')
    break

print(l)

for c in l:
    try:
        c_index = data.index(c)
        # Remove all values before character, as they can not be matches
        print(c, data)
        data = data[c_index+1:]
        print(data)
    except ValueError:
        # ValueError thrown if value does not match
        pass

    total += 1
    data.append(c)

    if len(data) == 14:
        break






print(data)
print(total)
