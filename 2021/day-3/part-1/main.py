#!/bin/python

class binary_diagnostic():
    _indexes = []
    _data_points = 0
    _initialized = False

    def __init__(self, data: list[str]):
        for _ in range(0, len(data[0])):
            self._indexes.append(0)

        print(f'Index length set to: {len(self._indexes)}')
        self.import_data(data)

    def import_data(self, data: list[str]):

        for d in data:
            # Keep track of the total data points
            self._data_points += 1

            for i, c in enumerate(d):
                if c == '1':
                    # Keep track of the number of '1's at each index
                    self._indexes[i] += 1

        print('Import finished.')
        print('Total imported:', self._data_points)
        print('Indexes:', self._indexes)

    def get_gamma_bits(self):
        res_arr = []
        for i in self._indexes:
            if i > self._data_points // 2:
                res_arr.append(1)
            else:
                res_arr.append(0)

        return res_arr

    def get_epsilon_bits(self):
        res_arr = []
        gamma_bits = self.get_gamma_bits()

        # Invert gamma
        for b in gamma_bits:
            if b == 0:
                res_arr.append(1)
            else:
                res_arr.append(0)

        return res_arr

    def get_gamma(self):
        return self._translate(self.get_gamma_bits())

    def get_epsilon(self):
        return self._translate(self.get_epsilon_bits())

    def _translate(self, bin: list[int]):
        bin = list(bin)
        bin.reverse()
        res = 0

        for i, b in enumerate(bin):
            res += b * pow(2, i)

        return res

    def get_power_consumption(self):
        return self.get_gamma() * self.get_epsilon()


def main():
    data = []
    for line in open('input.txt', 'r'):
        data.append(line.strip())

    diag = binary_diagnostic(data)

    print('Gamma bits', diag.get_gamma_bits())
    print('Epsilon bits', diag.get_epsilon_bits())

    print('Gamma', diag.get_gamma())
    print('Epsilon', diag.get_epsilon())

    print('Power consumption', diag.get_power_consumption())


if __name__ == "__main__":
    main()
