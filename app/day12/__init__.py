import string
import colorama

class Map(object):
    def __init__(self, data):
        self.data = data
        self.nodes = {}

        for row, cols in enumerate(data):
            for col, char in enumerate(cols):
                height = string.ascii_lowercase.index(char.replace('S', 'a').replace('E','z')) 
                self.nodes[str([row, col])] = {
                    'row': row,
                    'col': col,
                    'char': char,
                    'height': height, 
                    'visited': False,
                    'distance': None,
                    'via': None
                }
        
        self.rows = row+1
        self.cols = len(cols)

    def node(self, row, col):
        return self.nodes[str([row, col])] 
    
    def is_out_of_bounds(self, row, col):
        return any([
            row < 0,
            col < 0,
            row >= self.rows,
            col >= self.cols
        ])

    def neighbors(self, row, col):
        my_height = self.node(row, col)['height']
        candidates = []
        for o_row, o_col in ((-1, 0), (1,0), (0,-1), (0,1)):
            candidate = [row + o_row, col + o_col]

            if self.is_out_of_bounds(*candidate):
                #print(f'from {row}:{col} candidate {candidate} is out of bounds')
                pass
            elif self.node(*candidate)['visited']:
                #print(f'from {row}:{col} already visisted {candidate}')
                pass
            elif self.node(*candidate)['height'] - my_height > 1:
                #print(f'from {row}:{col} height difference to {candidate} is > 1')
                pass
            else:
                #print(f'from {row}:{col} {candidate} is valid')
                candidates.append(self.node(*candidate))

        return candidates
    
    def update_distance(self, row, col, distance, via):
        node = self.node(row, col)
        if not node['distance'] or distance < node['distance']:
            #print(f'updating distance for {row}:{col} distance={distance} via={via}')
            node['distance'] = distance
            node['via'] = via 

    def find_char(self, char):
        for row, cols in enumerate(self.data):
            if char in cols:
                return row, cols.index(char)
    
    def find_nodes_with_height(self, height):
        return [(node['row'], node['col']) for node in self.nodes.values() if node['height']==0]
    
    def solve(self, start_pos=None):
        self.start = self.node(*start_pos) if start_pos else self.node(*self.find_char('S'))
        self.end = self.node(*self.find_char('E'))

        self.update_distance(self.start['row'], self.start['col'], 0, None)
        current = self.start 

        while current:
            for neighbor in self.neighbors(current['row'], current['col']):
                self.update_distance(neighbor['row'], neighbor['col'], current['distance']+1, (current['row'], current['col']))

            current['visited'] = True 

            neighbors = sorted([node for node in self.nodes.values() if not node['visited'] and node['distance']], key=lambda x: x['distance'])
            
            if not neighbors:
                break

            current = neighbors[0]

        path = []
        node = self.end
        while node:
            path.append(node)
            if not node['via']:
                break;

            node = self.node(*node['via'])

        self.print_map(path)
        print(self.end)
        return self.end['distance']

    def print_map(self, path=None):
        for row in range(self.rows):
            line = [] 
            for col in range(self.cols):
                color = None
                node = self.node(row, col)
                if node in (self.start, self.end):
                    c = node['char'] 
                    color = colorama.Fore.GREEN if node == self.start else colorama.Fore.RED
                elif node in path:
                    c = '#'
                    color = colorama.Fore.GREEN
                else:
                    c = node['char']

                if not color and node['visited']:
                    color = colorama.Fore.YELLOW
                
                if color: 
                    c = color + c + colorama.Fore.RESET
                
                line.append(c)
            print(''.join(line))
            
def get_data(filename):
    map = []

    for line in open(filename, 'rt').read().split('\n'):
        map.append([c for c in line])

    return map    

def solve_part_1(filename):
    data = get_data(filename)
    map = Map(data)
    return map.solve()

def solve_part_2(filename):
    data = get_data(filename)

    results = [] 
    map = Map(data)
    for row, col in map.find_nodes_with_height(0):
        print(f'Solving part 2 with {row}:{col}')
        map2 = Map(data)
        distance = map2.solve((row,col))
        if distance:
            results.append(distance)
        
    print(f'part 2 results: {results}')
    print(f'part 2 min: {min(results)}')
    return min(results)

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 31:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 423:
        raise ValueError("Test Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == 29:
        raise ValueError("Tests Failed")

    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 416:
        raise ValueError("Test Failed")