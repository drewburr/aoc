#!/bin/python

class binary_diagnostic():
    _initialized = False

    def __init__(self, data: list[str]):

        self.DATA_COUNT = len(data)
        self.DATA_LENGTH = len(data[0])
        self.DATA = data

    def filter_on_index(self, data: list[str], index: int):
        """
        Splits data[str] into two lists, based on the value at index
        Returns (zeroes[str], ones[str])
        """
        zeroes = list(filter(lambda d: d[index] == '0', data))
        ones = list(filter(lambda d: d[index] == '1', data))
        return (zeroes, ones)

    def get_generator_rating(self):

        data = list(self.DATA)

        for i in range(len(data)):
            zeroes, ones = self.filter_on_index(data, i)
            if len(zeroes) > len(ones):
                data = zeroes
            else:
                data = ones

            if len(data) == 1:
                return data[0]

        raise Exception('Could not find unique generator result!', data)

    def get_scrubber_rating(self):

        data = list(self.DATA)

        for i in range(len(data)):
            zeroes, ones = self.filter_on_index(data, i)
            if len(zeroes) <= len(ones):
                data = zeroes
            else:
                data = ones

            if len(data) == 1:
                return data[0]

        raise Exception('Could not find unique scrubber result!', data)

    def _translate(self, bin: str | list[str | int]) -> int:
        """
        Converts a sequence of binary data into anint
        """
        bin = list(bin)
        bin.reverse()
        res = 0

        for i, b in enumerate(bin):
            res += int(b) * pow(2, i)

        return res

    def get_life_support_rating(self):
        return self._translate(self.get_generator_rating()) * self._translate(self.get_scrubber_rating())


def main():
    data = []
    for line in open('input.txt', 'r'):
        data.append(line.strip())

    diag = binary_diagnostic(data)

    print('Generator:', diag.get_generator_rating())
    print('Scrubber:', diag.get_scrubber_rating())
    print('Life Support Rating:', diag.get_life_support_rating())


if __name__ == "__main__":
    main()
