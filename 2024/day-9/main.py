input_file = "input.txt"
# input_file = "example.txt"

from operator import add, sub

part = 2

data: str = ''


for l in open(input_file):
    l = l.strip()
    data = l

disk: list[str] = list()

id_index = 0
for i, c in enumerate(data):
    if i % 2 == 0:
        char = id_index
        id_index += 1
    else:
        char = '.'

    for _ in range(int(c)):
        disk.append(char)

n_disk = disk.copy()

if part == 1:
    print('part one!')
    for i, c in enumerate(disk):
        while n_disk[-1] == '.':
            n_disk.pop()

        if c == '.':
            n_disk[i] = n_disk.pop()
        elif i > len(n_disk):
            break

else:
    for x in range(n_disk[-1], 0, -1):
        # print(n_disk)
        # print('x', x)
        index = n_disk.index(x)
        count = n_disk.count(x)

        # print('index', index)
        # print('count', count)

        for s in range(index):
            # if all spaces are empty
            slide = n_disk[s:s+count]
            # print(slide)
            if slide.count('.') == count:
                # print(count, x)
                for i in range(count):
                    n_disk[s+i] = n_disk[index+i]
                    n_disk[index+i] = '.'

                break

        while n_disk[-1] == '.':
            n_disk.pop()



print(disk)
print(n_disk)

total = 0
for i, c in enumerate(n_disk):
    if c != '.':
        total += i * int(c)

print(total)
