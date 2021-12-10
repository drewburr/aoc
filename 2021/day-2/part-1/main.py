#!/bin/python

class Submarine():

    def __init__(self):
        self._depth = 0
        self._horizontal = 0

    def add_horizontal(self, val: int):
        """
        Change the submarine's horizontal position
        """
        self._depth += val

    def add_depth(self, val: int):
        """
        Change the submarine's depth
        """
        self._horizontal += val

    def multiply(self) -> int:
        return self._depth * self._horizontal


def main():
    submarine: Submarine = Submarine()
    val: int
    direction: str

    path_dict = {
        "up": {
            "func": submarine.add_depth,
            "mod": -1
        },
        "down": {
            "func": submarine.add_depth,
            "mod": 1
        },
        "forward": {
            "func": submarine.add_horizontal,
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
