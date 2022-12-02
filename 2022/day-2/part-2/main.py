data = []
carry = []


WON = 6
DRAW = 3
LOST = 0

VAL_MAP = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

WIN_MAP = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

TIE_MAP = {
    'A': 'X', #Rock
    'B': 'Y', #Paper
    'C': 'Z'  #Sissors
}

LOSS_MAP = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'

}

for l in open('input.txt'):
    l = l.strip()

    data.append(l.split(' '))

print(data)

total = 0

for a, r in data:
    if r == 'X':
        b = LOSS_MAP[a]
    elif r == 'Y':
        b = TIE_MAP[a]
    elif r == 'Z':
        b = WIN_MAP[a]



    print(a,b)
    g_total = VAL_MAP[b]
    if TIE_MAP[a] == b: # tie
        print('tie')
        g_total += DRAW
    elif WIN_MAP[a] == b: # win
        print('win')
        g_total += WON


    total += g_total


print(total)


# ac = sorted(sum(c) for c in data)

# print(sum(ac[-3:]))



# t = sum(c)
# if t > mc:
#     mc = t
#     mi = i

# print(mc, mi)
