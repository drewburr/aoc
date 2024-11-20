input_file = 'input.txt'

part = 2

data = []

# Get a sorted list of dimentions
for l in open(input_file):
    l = l.strip()

    dims = list(map(int, l.split('x')))
    dims.sort()
    data.append(dims)

total = 0

for d in data:
    l, w, h = d[0], d[1], d[2]
    if part == 1:
        s_area = 2*l*w + 2*w*h + 2*h*l
        slack = l*w
        print(s_area + slack)
        total += s_area + slack
    else:
        perim = 2 *(l+w)
        volume = l*w*h
        print(perim + volume)
        total += (perim + volume)


print(total)
