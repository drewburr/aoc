input_file = "input.txt"
# input_file = "example.txt"

part = 2

reports = []

for l in open(input_file):
    l = l.strip()

    r = list(map(int, l.split(" ")))
    reports.append(r)

def is_safe(r: list[int]):
    # Define slope direction
    sign = 1 if r[0] > r[1] else -1

    last = r[0]
    for i, x in enumerate(r[1:]):
        # print(r)
        # Calculate slope
        slope = (last-x) * sign
        if slope <= 0:
            # print(r)
            print("wrong slope", slope, '(%s, %s)' % (last, x))
            return False, i

        if slope > 3:
            print(r)
            print("slope too high", slope, '(%s, %s)' % (last, x))
            return False, i

        last = x

    # Report is safe
    return True, None

def is_safe_dampened(r: list[int]):
    safe, i = is_safe(r)


    if not safe:
        for i in range(len(r)):
            r2 = r.copy()
            r2.pop(i)
            safe, _ = is_safe(r2)
            if safe:
                break

    if not safe:
        print('not safe')
    else:
        print('safe')

    return safe


total = 0

for report in reports:
    if part == 1:
        safe, _ = is_safe(report)
    else:
        safe = is_safe_dampened(report)

    if safe:
        total += 1

print(total)

# low: 644
# low: 647
# wrong: 655
