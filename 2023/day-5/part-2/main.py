input_file = "input.txt"

from bisect import bisect, insort

class MapItem:
    def __init__(self, dest: int, source: int, length: int):
        self.dest = dest
        self.source = source
        self.length = length

    def translate(self, x: int):
        if x in self:
            offset = x - self.source
            return self.dest + offset

        return None

    def __str__(self):
        return f"MapItem[Source({self.source}, {self.source+self.length}), Dest({self.dest}, {self.dest+self.length})]"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, g):
        return {"source": self.source, "dest": self.dest, "length": self.length}.get(g)

    def __lt__(self, other):
        if isinstance(other, int):
            return self.source < other

        return self.source < other.source

    def __gt__(self, other):
        if isinstance(other, int):
            return (self.source + self.length) > other

        return self.source > other.source

    def __eq__(self, x):
        return x in self

    def __ne__(self, x):
        return not self == x

    def __contains__(self, x):
        return x >= self.source and x < (self.source + self.length)


seeds = []
seed_soil: list[MapItem] = []
soil_fertilizer: list[MapItem] = []
fertilizer_water: list[MapItem] = []
water_light: list[MapItem] = []
light_temperature: list[MapItem] = []
temperature_humidity: list[MapItem] = []
humidity_location: list[MapItem] = []

mapitems_list = [
    seed_soil,
    soil_fertilizer,
    fertilizer_water,
    water_light,
    light_temperature,
    temperature_humidity,
    humidity_location,
]


def parse_input():
    input_obj: list[dict] = None
    input_list = list(mapitems_list)
    l: str
    global seeds
    for l in open(input_file):
        l = l.strip()
        if not l:
            continue

        if l.find(":") != -1:
            if not seeds:
                seeds = [int(x) for x in l.split(':')[1].split()]
            else:
                input_obj = input_list.pop(0)
            continue

        item = MapItem(*[int(x) for x in l.split()])

        insort(input_obj, item)

def translate_seed(value):
    for mapitems in mapitems_list:
        # print(mapitems)
        mapped_value = map_value(mapitems, value)
        # print(f"{value}->{mapped_value}")
        value = mapped_value

    # print(" ")
    return value


def map_value(mapitems: list[MapItem], value):
    item_i = bisect(mapitems, value)
    if item_i == len(mapitems):
        return value

    return mapitems[item_i].translate(value) or value


def main():
    parse_input()

    smallest = float('inf')
    for i, s in enumerate(seeds):
        if i % 2:
            continue

        length = seeds[i+1]
        locations = [translate_seed(x) for x in range(s, s+length)]

        # print(len(locations), locations)

        v = min(locations)

        if v < smallest:
            smallest = v

    print(smallest)


if __name__ == "__main__":
    main()
