import re


input_file = "input.txt"
input_file = "example.txt"

part = 2

raw = 0
true = 0

for l in open(input_file):
    l = l.strip()

    raw += len(l)
    true += len(eval(l))

    print(len(l), len(eval(l)), len(l.encode()))

    new = '"%s"'.format(l)

    print(l, eval(l), re.escape(new))

print(raw - true)
