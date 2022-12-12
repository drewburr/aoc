def main():

    monkeys: dict[int, Monkey] = {}

    with open('sample.txt') as f:
        raw = f.readlines()
        data = list(map(lambda l: l.strip(), raw))

    indexes = map(lambda v: v[7], data[0::7])
    items = map(lambda v: v.replace(',', '').split(' ')[2:], data[1::7])
    operations = map(lambda v: v.split(' ')[4:], data[2::7])
    div_tests = map(lambda v: v.split(' ')[-1], data[3::7])
    trues = map(lambda v: v.split(' ')[-1], data[4::7])
    falses = map(lambda v: v.split(' ')[-1], data[5::7])

    monkey_data = zip(indexes, items, operations, div_tests, trues, falses)

    for args in monkey_data:
        index = args[0]
        monkeys[int(index)] = Monkey(*args[1:])

    # 20 rounds
    for i in range(20):
        # Process all items on every monkey
        for monkey in monkeys.values():
            while monkey.has_items():
                item, thrown_to = monkey.inspect_item()
                monkeys[thrown_to].add_item(item)

        print(f'Round {i} complete')

        for i, monkey in monkeys.items():
            print('Monkey', i, monkey.items)

        print()

    all_business = []

    for monkey in monkeys.values():
        all_business.append(monkey.business)

    all_business.sort()

    print(all_business[-1] * all_business[-2])


class Monkey():
    def __init__(self, items, operation: list[str], div_test, true_res, false_res):
        unfactored_items = map(int, items)
        self.items = list(map(self.factorize, unfactored_items))
        self.operation = operation
        self.div_test = int(div_test) # Always a prime number
        self.true_res = int(true_res)
        self.false_res = int(false_res)
        self.business = 0

    def inspect_item(self):
        self.business += 1

        item = self.items.pop(0)
        worry = self.calculate_worry(item)

        if self.is_divisible(worry):
            # Divisible
            return worry, self.true_res
        else:
            # Not divisible
            return worry, self.false_res


    def is_divisible(self, item):
        # Is divisible when factor is present
        if self.div_test in item:
            return True
        else:
            return False

    def calculate_worry(self, item):
        operand = self.operation[0]
        value = self.operation[1]

        if operand == '*':
            if value == 'old':
                value = value * 2
            else:
                # Value is always a prime number, no need to factor
                item.append(int(value))
        elif operand == '+':
            # Multiply all factors together
            total = 1
            for v in item:
                total *= v
            # Then add value
            total += int(value)
            # Finally, refactor value
            item = self.factorize(total)
        else:
            raise Exception()

        return item

    def add_item(self, item):
        self.items.append(item)

    def has_items(self):
        if self.items:
            return True
        else:
            return False

    def factorize(self, val: int):
        """
        Return a list of all factors of a number
        """
        factors = list()
        i = 2

        while i * i <= val:
            while val % i == 0:
                factors.append(i)
                val = val // i
            i = i + 1

        if val > 1:
            factors.append(val)

        return factors

if __name__ == "__main__":
    main()
