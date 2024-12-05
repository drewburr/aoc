import re

input_file = "input.txt"
# input_file = "example.txt"

part = 2

rules: list[list[str]] = []
pages: list[list[str]] = []

processingRules = True
for l in open(input_file):
    l = l.strip()

    if not l:
        processingRules = False
        continue

    if processingRules:
        rules.append(l.split('|'))
    else:
        pages.append(l.split(','))


def passes_rules(p: list[str]):
    for r1, r2 in rules:
        if p.count(r1) and p.count(r2):
            # Check if rule is broken
            if p.index(r1) > p.index(r2):
                # print('fail', p, (r1, r2))
                return False

    return True

def fix_page(_page: list[str]):
    p = _page.copy()
    # print(p)
    for r1, r2 in rules:
        if p.count(r1) and p.count(r2):
            i1 = p.index(r1)
            i2 = p.index(r2)

            if i1 > i2:
                # Move right value to the left of the left value
                p.insert(i1, p.pop(i2))

    return p





passedTotal = 0
fixedTotal = 0
for p in pages:
    mid = (len(p)) // 2
    if passes_rules(p):
        # print('pass', p, p[mid])
        passedTotal += int(p[mid])
    else:
        while not passes_rules(p):
            p = fix_page(p)

        fixedTotal += int(p[mid])

print(passedTotal)
print(fixedTotal)
