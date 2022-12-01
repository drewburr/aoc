data = []
carry = []

for l in open('input.txt'):
    l = l.strip()

    if l:
        carry.append(int(l))
    else:
        data.append(carry)
        carry = []


ac = sorted(sum(c) for c in data)

print(sum(ac[-3:]))

# t = sum(c)
# if t > mc:
#     mc = t
#     mi = i

# print(mc, mi)
