input_file = 'example.txt'

data = []

for l in open(input_file):
    l = l.strip()

    data.append(list(filter(str.isnumeric, l)))


# Data is a list of iterable filter objects
answer = 0

for d in data:
    derived = int(d[0] + d[-1])
    answer += derived

print(answer)
