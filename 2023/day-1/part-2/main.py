input_file = 'input.txt'

lines: list[str] = []
data = []


class Lineparser():
    min_text_length = 3
    max_text_length = 5

    def __init__(self):
        self.first = None
        self.last = None

    def gettextdigit(self, x: str):
        # Checks if a string is a spelled digit. Returnes value of found digit
        string_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}

        if val := string_digits.get(x):
            # print('Found', x)
            return val
        return None

    def parsedigit(self, x: str):
        # Takes in a string and recusrively parses out a text-based digit
        # i is the frame, and j is the offset
        for i in range(self.min_text_length, self.max_text_length+1):
            for j in range(len(x)-i+1):
                if len(x) >= i and (val := self.gettextdigit(x[j:i+j])):
                    return val

    def parseline(self, l: str):
        text_list = list()
        for c in l:
            text = ''
            # Finding a numeric digit resets the letters
            if c.isdigit():
                self.storedigit(c)
                text_list = list()
                continue
            else:
                text_list.append(c)
                text = ''.join(text_list)

            print(text)

            # There are enough letters to form a potential string digit
            if len(text) >= self.min_text_length:
                if val := self.parsedigit(text):
                    self.storedigit(str(val))
                    text_list.pop(0) # Remove first letter, since digit was found

                # Remove first letter if no word was found, and length is met
                elif len(text) == self.max_text_length:
                    text_list.pop(0)

        print(self.first, self.last, '\n')
        return self.first + (self.last or self.first)

    def storedigit(self, x):
        print('Storing', x)
        if self.first:
            self.last = x
        else:
            self.first = x



for l in open(input_file):
    l = l.strip()
    lines.append(l)

# Parsing out numeric digits and string digits
for i, l in enumerate(lines):
    # Storing letters to be parsed
    print('Line', i+1)
    parser = Lineparser()
    result = parser.parseline(l)
    data.append(result)




# Data is a list of string-integers
print(data)
answer = sum([int(x) for x in data])

# for d in data:
#     derived = int(d[0] + d[-1])
#     answer += derived

print(answer)
