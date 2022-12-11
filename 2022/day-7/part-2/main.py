data = []
total = 0

SIZE_LIMIT = 100000
SIZE_KEY = '_size'

TOTAL_DISK = 70000000
MIN_DISK = 30000000

def main():
    machine = Machine()

    for l in open('input.txt'):
        l = l.replace('\n', '')
        data = l.split(' ')

        print(data)

        if data[0] == '$':
            process_func = False
            # Handle command
            cmd = data[1]
            command_map = {
                'cd': machine.cd,
                'ls': machine.ls
            }

            # Map passed command to a function, and store for later use
            process_func = command_map[cmd]
            # Call in case processing is needed
            process_func(data[2:])
        else:
            process_func(data)

    print(machine.root)

    machine.calculate_sizes()

    print(machine.get_answer())






class Machine():
    def __init__(self):
        self.root = {}
        self.path = []
        self.cwd = {}
        self.process_func = None
        self.dir_sizes = []

    def calculate_sizes(self, cwd=None):
        if not cwd:
            cwd = self.root

        if not cwd.get(SIZE_KEY):
            val = 0
        else:
            val = cwd.pop(SIZE_KEY)

        for nwd in cwd.values():
            val += self.calculate_sizes(nwd)

        self.dir_sizes.append(val)

        return val

    def get_answer(self):

        self.dir_sizes.sort()

        total_size = self.dir_sizes[-1] # Biggest size is always root

        unused_disk = TOTAL_DISK - total_size

        print('unused disk:', unused_disk)
        print('need to free:', unused_disk - MIN_DISK)

        for s in self.dir_sizes:
            print(unused_disk + s)
            # If deleting this dir gets us below the min
            if (unused_disk + s) >= MIN_DISK:
                return s



my_dict = {}
my_dict['a'] = {}
my_a = my_dict['a']
print(my_a)
print(my_dict)
my_a['hello'] = 'world'
print(my_a)
print(my_dict)



    def cd(self, dir: str):
        dir = dir[0]
        print('cd', dir)
        if (dir == '/'):
            # Reset to root
            self.path = [self.root]
            self.cwd = self.root
        elif (dir == '..'):
            # Move back a directory
            self.cwd = self.path.pop(-1)
        else:
            # Store cwd in path stack
            # Then update cwd
            self.path.append(self.cwd)
            self.cwd = self.cwd[dir]


    def ls(self, *args):
        if not args[0]:
            return
        values = args[0]

        print('ls', values)

        if values[0] == 'dir':
            # dir e
            self.mkdir(values[1])
        else:
            # 2557 g
            self.touch(values[0])


    def mkdir(self, name: str):
        """Create a directory"""
        if not self.cwd.get(name):
            self.cwd[name] = {}

    def touch(self, size: str):
        """
        Store file data
        We don't care about file names, so we're not storing them
        """
        if not self.cwd.get(SIZE_KEY):
            self.cwd[SIZE_KEY] = 0

        self.cwd[SIZE_KEY] += int(size)


main()
