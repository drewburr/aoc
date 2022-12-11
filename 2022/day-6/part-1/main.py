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
        data = data[c_index+1:]
        data.append(c)
    except ValueError:
        # ValueError thrown if value does not match
        if len(data) == 4:
            break
        else:
            data.append(c)

    total += 1




print(data)
print(total)
