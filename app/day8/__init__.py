import math

def get_data(filename):
    return open(filename, 'rt').read()

def get_trees_around(data, row, col):
    left = list(map(int, data[row][:col]))
    right = list(map(int, data[row][col+1:]))
    above = [int(data[x][col]) for x in range(0, row)]
    below = [int(data[x][col]) for x in range(row+1, len(data))]

    return (left, right, above, below)

def is_visible_from_edge(data, row, col):
    h = int(data[row][col]) 
    left, right, above, below = get_trees_around(data, row, col)

    if any([
        row == 0 or row == len(data)-1 or col == 0 or col == len(data[row])-1,
        len(left) and max([x for x in left]) < h,
        len(right) and max([x for x in right]) < h,
        len(above) and max([x for x in above]) < h,
        len(below) and max([x for x in below]) < h
    ]):
        return True

def get_science_score(data, row, col):
    h = int(data[row][col]) 
    left, right, above, below = get_trees_around(data, row, col)

    scores = []
    for trees in [list(reversed(above)), list(reversed(left)), below, right]:
        score = 0
        last = 0 

        for t in trees: 
            score += 1

            if t >= h:
                break

        if score:
            scores.append(score)

    total_score = math.prod(scores) 

    return total_score

def solve_part_1(filename):
    data = get_data(filename).split('\n')

    visible = 0

    for row in range(0, len(data)):
        for col in range(0, len(data[row])): 
            if is_visible_from_edge(data, row, col):
                visible += 1

    print(f'solve part 1: visible {visible}')
    return visible 

def solve_part_2(filename):
    data = get_data(filename).split('\n')

    best_score = 0
    for row in range(0, len(data)):
        for col in range(0, len(data[row])): 
            science_score = get_science_score(data, row, col)
            best_score = max([science_score, best_score])
    
    print(f'solve part 2: best score {best_score}')
    return best_score

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 21:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 1829:
        raise ValueError("Test Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == 16:
        raise ValueError("Tests Failed")

    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 291840:
        raise ValueError("Test Failed")