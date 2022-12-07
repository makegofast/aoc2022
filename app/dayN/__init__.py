def get_data(filename):
    return open(filename, 'rt').read()

def solve_part_1(filename):
    pass

def solve_part_2(filename):
    pass

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 0:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 0:
        raise ValueError("Test Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == 0:
        raise ValueError("Tests Failed")


    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 0:
        raise ValueError("Test Failed")