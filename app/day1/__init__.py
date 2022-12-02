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

class day_1(object):
    @staticmethod
    def get_data(filename):
        for line in open(filename, 'rt'):
            yield line.strip()

    def solve(self, filename):
        data = self.get_data(filename)

        buffer = []

        elves = Elves()
        elf = Elf()
        for line in data:
            if line == "":
                elves.add_elf(elf)
                elf = Elf()
            else:
                elf.add_ration(line)

        elves.add_elf(elf)

        print(f'part 1: {elves.sum_top_calories(1)}')
        print(f'part 2: {elves.sum_top_calories(3)}')

if __name__ == "__main__":
    day1 = day_1()
    day1.solve('test_data.txt')
    day1.solve('data.txt')
