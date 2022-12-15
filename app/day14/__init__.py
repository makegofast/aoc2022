import math
import itertools

class Cave(object):
    def __init__(self, rock_data, part_2_rules=False):
        self.part_2_rules = part_2_rules
        self.tiles = {}
        self.grain = None

        self.set_tile(0, 500, '+')
        self.load_rock_data(rock_data)

        self.update_minmax()

        while self.tick() != False:
            pass

        self.print_tiles()
    
    def load_rock_data(self, rock_data):
        for points in rock_data:
            for start, end in itertools.pairwise(points):
                for row, col in self.expand_points(start, end):
                    self.set_tile(row, col, '#')

    def update_minmax(self):
        self.min_row = 0
        self.max_row = max(self.tiles.keys())
        self.min_col = min([min(c.keys()) for c in self.tiles.values()])
        self.max_col = max([max(c.keys()) for c in self.tiles.values()])

    def expand_points(self, start, end):
        min_c, max_c = min(start[0], end[0]), max(start[0], end[0])
        min_r, max_r = min(start[1], end[1]), max(start[1], end[1])

        for c in range(min_c, max_c+1):
            for r in range(min_r, max_r+1):
                yield (r, c)

    def get_tile(self, row, col):
        if self.grain == [row, col]:
            return 'O'
        
        if self.part_2_rules and row == self.max_row + 2:
            return '#'

        return self.tiles.get(row, {}).get(col, '.')

    def set_tile(self, row, col, tile):
        self.tiles.setdefault(row, {})
        self.tiles[row][col] = tile

        #if hasattr(self, 'min_col') and col < self.min_col:
        #    self.min_col = col

        #if hasattr(self, 'max_col') and col > self.max_col:
        #    self.max_col = col

    def print_tiles(self):
        self.update_minmax()

        for row in range(0, self.max_row+10):
            chars = [self.get_tile(row, col) for col in range(self.min_col-20, self.max_col+21)]
            print(str(row) + ' ' + ''.join(chars))
    
    def out_of_bounds(self, row, col):
        if self.part_2_rules:
            return row > self.max_row + 2
        else:
            return row > self.max_row or col < self.min_col or col > self.max_col 

    def tick(self):
        if not self.grain:
            if self.get_tile(0, 500) == 'o':
                return False

            self.grain = [0, 500]

        return self.move_grain()

    def move_grain(self):
        current = self.grain
        candidates = [1,0], [1,-1], [1,1]
        for candidate in candidates:
            new = current[0]+candidate[0], current[1]+candidate[1] 

            if self.out_of_bounds(*new):
                return False

            if self.get_tile(*new) == '.':
                self.grain = new
                return
        
        self.set_tile(current[0], current[1], 'o')
        self.grain = None
    
    def count_grains(self):
        ret = 0
        for row in self.tiles.values():
            for tile in row.values():
                ret += tile == 'o'

        return ret
    
def get_data(filename):
    ret = []
    for line in open(filename, 'rt').read().split('\n'):
        ret.append([list(map(int, p.split(','))) for p in line.split(' -> ')])
    
    return ret

def solve_part_1(filename):
    data = get_data(filename)
    cave = Cave(data)
    grain_count = cave.count_grains()
    print(f'part 1 gains={grain_count}')
    return grain_count

def solve_part_2(filename):
    data = get_data(filename)
    cave = Cave(data, part_2_rules=True)
    grain_count = cave.count_grains()
    print(f'part 1 gains={grain_count}')
    return grain_count

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 24:
        raise ValueError("Part 1 Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 692:
        raise ValueError("Part 1 Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == 93:
        raise ValueError("Part 2 Tests Failed")

    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 0:
        raise ValueError("Part 2 Failed")