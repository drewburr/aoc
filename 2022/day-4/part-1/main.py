data = []
total = 0

for l in open('input.txt'):
    l = l.strip()

    r1, r2 = l.split(',')
    r1 = tuple(map(int, r1.split('-')))
    r2 =tuple(map(int, r2.split('-')))

    print(list(zip(r1, r2)))

    if r1[0] <= r2[0] and r1[1] >= r2[1]:
        print('found!')
        total += 1
    elif r1[0] >= r2[0] and r1[1] <= r2[1]:
        print('found!')
        total += 1


print(total)
