class Elf(object):
    def __init__(self):
       self.rations = []

    def add_ration(self, calorieCount):
       self.rations.append(int(calorieCount))

    @property
    def total_rations(self):
        return sum(self.rations)

class Elves(object):
    def __init__(self):
        self.elves = []

    def add_elf(self, elf):
        self.elves.append(elf)

    def sum_top_calories(self, count):
        return sum([e.total_rations for e in sorted(self.elves, key=lambda x: x.total_rations)[-count:]])

class Solver(object):
    @staticmethod
    def get_data(filename):
        with open(filename, 'rt') as fp:
            for line in fp:
                yield line.strip()

    def solve(self, filename):
        data = self.get_data(filename)

        elves = Elves()
        elf = Elf()
        for line in data:
            if line == "":
                elves.add_elf(elf)
                elf = Elf()
            else:
                elf.add_ration(line)

        elves.add_elf(elf)

        part1 = elves.sum_top_calories(1)
        print(f'part 1: {part1}')

        part2 = elves.sum_top_calories(3)
        print(f'part 2: {part2}') 

        return (part1, part2)


if __name__ == "__main__":
    solver = Solver()
    print("Running Tests...")
    if not solver.solve('test_data.txt') == (24000, 45000):
        raise ValueError("Tests Failed")

    print("Solving...")
    solver = Solver()
    solver.solve('data.txt')