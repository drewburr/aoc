def main():

    monkeys: dict[int, Monkey] = {}

    with open('input.txt') as f:
        raw = f.readlines()
        data = list(map(lambda l: l.strip(), raw))

    indexes = map(lambda v: v[7], data[0::7])
    items = map(lambda v: v.replace(',','').split(' ')[2:], data[1::7])
    operations = map(lambda v: ' '.join(v.split(' ')[3:]), data[2::7])
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
        self.items = list(map(int, items))
        self.operation = operation
        self.div_test = int(div_test)
        self.true_res = int(true_res)
        self.false_res = int(false_res)
        self.business = 0

    def inspect_item(self):
        self.business += 1

        item = self.items.pop(0)
        worry = self.calculate_worry(item) // 3

        if worry % self.div_test:
            # Not divisible
            return worry, self.false_res
        else:
            # Divisible
            return worry, self.true_res


    def calculate_worry(self, item):
        old = item
        new = eval(self.operation)
        return new

    def add_item(self, item):
        self.items.append(item)

    def has_items(self):
        if self.items:
            return True
        else:
            return False

main()
