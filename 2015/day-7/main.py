from bitarray import bitarray

input_file = "input.txt"
# input_file = "example.txt"

part = 2


class Instruction:
    def __init__(self, command, register):
        self.command: str = command
        self.register: list[int] = register


class Instructions:
    def __init__(self):
        # Registers to instructions
        self._definitions: dict[str, Instruction] = {}

    def add(self, inst: Instruction):
        self._definitions[inst.register] = inst

    def get(self, register: str):
        """
        Provide the command required to define a register
        """
        return self._definitions.get(register)


class Machine:
    def __init__(self, instuctions: Instructions):
        self.reg: dict[str, int | tuple[function, tuple[str]]] = {}
        self.ops: dict[str, function] = {
            "COPY": self._copy,
            "NOT": self._not,
            "AND": self._and,
            "OR": self._or,
            "LSHIFT": self._lshift,
            "RSHIFT": self._rshift,
        }
        # Ordered list of instructions required to build
        self._stack = []
        self._instructions = instuctions

    def operate(self):
        self._generate()

        print("generate finished!")

        self._calculate()

        print("calculate finished!")

        print(self.reg["a"])

    def _calculate(self, register="a"):
        res = self.reg.get(register)
        print(res)
        if type(res) is int:
            return

        func = res[0]
        args = res[1]

        # Ensure all dependents are calculated
        for reg in args[:-1]:
            self._calculate(reg)

        # Fire when ready
        func(*args)

    def _generate(self, register="a"):
        # Skip if already in register
        if self.reg.get(register) is not None:
            print(register, "already defined")
            return

        print(register)
        inst = self._instructions.get(register)
        func, args = self._decode(inst)

        self.reg[register] = (func, args)

        for reg in args[:-1]:
            self._generate(reg)

    def _decode(self, inst: Instruction):
        """
        Takes Instruction, and returns the relevant
        function and its args as a tuple.
        Callable as func(*args)
        """
        c_len = len(inst.command)
        if c_len == 1:
            # lx -> a
            op = self.ops["COPY"]
            args = (inst.command[0], inst.register)
        elif c_len == 2:
            # NOT x -> h
            op = self.ops[inst.command[0]]
            args = (inst.command[1], inst.register)
        else:
            # x AND y -> d
            op = self.ops[inst.command[1]]
            args = (inst.command[0], inst.command[2], inst.register)

        return (op, args)

    def store(self, i, r):
        self.reg[r] = int(i)

    def _copy(self, x, r):
        self.reg[r] = self.reg[x]

    def _not(self, x, r):
        # Does a not, based on instructions
        # Python bitwise NOT is signed, and cannot be used
        self.reg[r] = self.reg[x] ^ (2**16 - 1)

    def _and(self, x, y, r):
        self.reg[r] = self.reg[x] & self.reg[y]

    def _or(self, x, y, r):
        self.reg[r] = self.reg[x] | self.reg[y]

    def _lshift(self, x, i, r):
        self.reg[r] = self.reg[x] << int(i)

    def _rshift(self, x, i, r):
        self.reg[r] = self.reg[x] >> int(i)


def get_machine():
    instructions = Instructions()
    machine = Machine(instructions)
    for l in open(input_file):
        l = l.strip()

        # if l:
        command, reg = l.split(" -> ")
        command = command.split(" ")

        if len(command) == 1 and command[0].isdecimal():
            machine.store(command[0], reg)
        else:
            ints = [c for c in command if c.isdigit()]
            for i in ints:
                machine.store(i, i)

            instructions.add(Instruction(command, reg))

    return machine


mach = get_machine()
mach.operate()

if part == 1:
    print(mach.reg["a"])
else:
    mach2 = get_machine()
    # Replace 'b' with 'a' and recompute
    mach2.store(mach.reg["a"], "b")
    mach2.operate()
    print(mach2.reg["a"])
