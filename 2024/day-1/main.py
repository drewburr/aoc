input_file = "input.txt"
# input_file = "example.txt"

part = 2
left = []
right = []

for l in open(input_file):
        l = l.strip()

        pair = l.split("   ")

        left.append(int(pair[0]))
        right.append(int(pair[1]))


left.sort()
right.sort()

pairs = zip(left, right)


total = 0

if part == 1:
    for l, r in pairs:
        total += abs(l - r)

else:
    for x in left:
        total += x * right.count(x)

print(total)
