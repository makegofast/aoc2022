class Solver(object):
    winning_combos = ['RP', 'PS', 'SR']
    shape_scores = {'R': 1, 'P': 2, 'S': 3}

    @staticmethod
    def get_data(filename):
        with open(filename, 'rt') as fp:
            while line := fp.readline().rstrip().split():
                yield line[0], line[1]

    @staticmethod
    def score_round(o, p):
        shape_score = Solver.shape_scores[p]

        if o == p:
            return 3 + shape_score 
        elif o+p in Solver.winning_combos:
            return 6 + shape_score
        else:
            return shape_score

    def solve_part_1(self, filename):
        crypt_map = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'} 
        score = 0

        for o, p in self.get_data(filename):
            o, p = (crypt_map[o], crypt_map[p]) 
            score += Solver.score_round(o, p)

        print(f'part 1 score: {score}')
        return score

    def solve_part_2(self, filename):
        crypt_map = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'L', 'Y': 'D', 'Z': 'W'} 
        winning_map = {'R': 'P', 'P': 'S', 'S': 'R'}
        losing_map  = {'R': 'S', 'P': 'R', 'S': 'P'}
        score = 0

        for o, r in self.get_data(filename):
            o, r = (crypt_map[o], crypt_map[r]) 
            
            if r == 'D':
                p = o
            elif r == 'W':
                p = winning_map[o]
            else:
                p = losing_map[o]

            score += Solver.score_round(o, p)

        print(f'part 2 score: {score}')
        return score

if __name__ == "__main__":
    solver = Solver()
    print("Running Test Part 1...")
    if not solver.solve_part_1('test_data.txt') == 15:
        raise ValueError("Tests Failed")

    solver = Solver()
    print("Running Test Part 2...")
    if not solver.solve_part_2('test_data.txt') == 12:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    solver = Solver()
    if not solver.solve_part_1('data.txt') == 13924:
        raise ValueError("Test Failed")

    print("Solving Part 2...")
    solver = Solver()
    if not solver.solve_part_2('data.txt') == 13448:
        raise ValueError("Test Failed")