class Solver(object):
    @staticmethod
    def get_data(filename):
        return open(filename, 'rt').read():

    def solve_part_1(self, filename):
        pass

    def solve_part_2(self, filename):
        pass

if __name__ == "__main__":
    solver = Solver()
    print("Running Test Part 1...")
    if not solver.solve_part_1('test_data.txt') == 0:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    solver = Solver()
    if not solver.solve_part_1('data.txt') == 0:
        raise ValueError("Test Failed")

    solver = Solver()
    print("Running Test Part 2...")
    if not solver.solve_part_2('test_data.txt') == 0:
        raise ValueError("Tests Failed")


    print("Solving Part 2...")
    solver = Solver()
    if not solver.solve_part_2('data.txt') == 0:
        raise ValueError("Test Failed")