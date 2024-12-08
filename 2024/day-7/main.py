input_file = "input.txt"
# input_file = "example.txt"

part = 2

data: list[dict] = []

for l in open(input_file):
    l = l.strip()
    v = l.split(": ")
    data.append({"res": int(v[0]), "values": v[1].split(" ")})


def custom_range(start, end=None, base=2, step=1):
    if not end:
        start, end = 0, start

    def Convert(n, out_len=None):
        string = "012"
        if n < base:
            v = string[n]
        else:
            v = Convert(n // base) + string[n % base]
        if out_len:
            adj = out_len - len(v) - 1
            v = ("0" * adj) + v
        return v

    out_len = len(Convert(end))
    return (Convert(i, out_len) for i in range(start, end, step))


operator = {"0": "+", "1": "*", "2": "", 0: "+", 1: "*", 2: ""}

if part == 1:
    base = 2
else:
    base = 3


def is_match(values, res, op_bits: str):
    # print(op_bits)
    e_res = values[0]
    for i, b in enumerate(op_bits, 1):
        if b != "2":
            e_res = eval(f"{e_res}{operator[b]}{values[i]}")
        else:
            e_res = eval(f"{e_res}{values[i]}")

    if e_res == res:
        return True

    return False


total = 0
for equation in data:
    res = equation["res"]
    values = equation["values"]
    # print(values, res)

    for op_bits in custom_range(base ** (len(values) - 1), base=base):
        if is_match(values, res, op_bits):
            total += res
            break

    # print()

print(total)
