class Solver(object):
    @staticmethod
    def get_data(filename):
        with open(filename, 'rt') as fp:
            while line := fp.readline().rstrip():
                yield line 

    @staticmethod
    def gen_list_from_range(range_str):
        start, stop = range_str.split('-')
        return set(range(int(start), int(stop)+1))

    def solve_part_1(self, filename):
        inclusive = 0
        for line in Solver.get_data(filename):
            ranges = line.split(',')
            a_set = Solver.gen_list_from_range(ranges[0])
            b_set = Solver.gen_list_from_range(ranges[1])
            inclusive += a_set.issubset(b_set) or b_set.issubset(a_set)
        
        print(f'part 1 inclusive count: {inclusive}')
        return inclusive

    def solve_part_2(self, filename):
        overlap = 0
        for line in Solver.get_data(filename):
            ranges = line.split(',')
            a_set = Solver.gen_list_from_range(ranges[0])
            b_set = Solver.gen_list_from_range(ranges[1])
            overlap += 1 if a_set.intersection(b_set) else 0 

        print(f'part 2 overlap: {overlap}')
        return overlap

if __name__ == "__main__":
    solver = Solver()
    print("Running Test Part 1...")
    if not solver.solve_part_1('test_data.txt') == 2:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    solver = Solver()
    if not solver.solve_part_1('data.txt') == 503:
        raise ValueError("Test Failed")

    solver = Solver()
    print("Running Test Part 2...")
    if not solver.solve_part_2('test_data.txt') == 4:
        raise ValueError("Tests Failed")

    print("Solving Part 2...")
    solver = Solver()
    if not solver.solve_part_2('data.txt') == 827:
        raise ValueError("Test Failed")