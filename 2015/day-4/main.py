import _md5

input_file = "input.txt"

part = 2
data = []

if part == 1:
    prefix = '00000'
else:
    prefix = '000000'

with open(input_file, "r") as f:
    input = f.read().strip()

num = 1
while True:
    encoded = (input + str(num)).encode("utf-8")
    res = _md5.md5(encoded).hexdigest()
    if res.startswith(prefix):
        print(res)
        print(num)
        break

    if num % 10000 == 0:
        print(num)
        # if num > 1000000:
            # break

    num += 1
