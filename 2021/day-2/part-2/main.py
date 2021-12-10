#!/bin/python

class Submarine():

    def __init__(self):
        self._aim = 0
        self._horizontal = 0
        self._vertical = 0

    def add_aim(self, val: int):
        """
        Change the submarine's currrent aim
        """
        self._aim += val

    def move(self, val: int):
        """
        Change the submarine's depth
        """
        self._horizontal += val
        self._vertical += val * self._aim

    def multiply(self) -> int:
        return self._vertical * self._horizontal


def main():
    submarine: Submarine = Submarine()

    path_dict = {
        "up": {
            "func": submarine.add_aim,
            "mod": -1
        },
        "down": {
            "func": submarine.add_aim,
            "mod": 1
        },
        "forward": {
            "func": submarine.move,
            "mod": 1
        }
    }

    for line in open('input.txt', 'r'):
        direction, str_val = line.split(' ')

        func = path_dict[direction]['func']
        value = int(str_val) * path_dict[direction]['mod']

        func(value)

    print(submarine.multiply())


if __name__ == "__main__":
    main()
