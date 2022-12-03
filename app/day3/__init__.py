class Solver(object):
    @staticmethod
    def get_data(filename):
        with open(filename, 'rt') as fp:
            while line := fp.readline().rstrip():
                yield line

    @staticmethod
    def priority(c):
        pmap = [chr(i) for i in list(range(97,123)) + list(range(65,91))]
        return pmap.index(c) + 1

    def solve_part_1(self, filename):
        sp = 0
        for line in Solver.get_data(filename):
            c1, c2 = line[:len(line)//2], line[len(line)//2:]
            common = set.intersection(set(c1), set(c2))
            for c in common:
                sp += Solver.priority(c)

        print(f'part 1 sum: {sp}')
        return sp

    def solve_part_2(self, filename):
        sp = 0
        group = []
        for line in Solver.get_data(filename):
            print(f'appending {line}')
            group.append(line)
        
            if len(group) == 3:
                common = set.intersection(*[set(g) for g in group])
                for c in common:
                    p = Solver.priority(c)
                    sp += p
                    print(f'group p {c} {p} (sp {sp})')
                    
                group = []

        print(f'part 2 sum: {sp}')
        return sp 

if __name__ == "__main__":
    solver = Solver()
    print("Running Test Part 1...")
    if not solver.solve_part_1('test_data.txt') == 157:
        raise ValueError("Tests Failed")

    solver = Solver()
    print("Running Test Part 2...")
    if not solver.solve_part_2('test_data.txt') == 70:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    solver = Solver()
    if not solver.solve_part_1('data.txt') == 7824:
        raise ValueError("Test Failed")

    print("Solving Part 2...")
    solver = Solver()
    if not solver.solve_part_2('data.txt') == 2798:
        raise ValueError("Test Failed")