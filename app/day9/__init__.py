class RopeKnot(object):
    def __init__(self, parent=None):
        self.position = [0,0]
        self.parent = parent
        self.child = None
        self.visited = [self.position] 
        self.id = parent.id + 1 if parent else 0
        
        print(f'node {self.id} is alive!')

    def tail(self):
        return self.child.tail() if self.child else self

    def get_field_bounds(self):
        x_vals = [v[0] for v in self.visited]
        y_vals = [v[1] for v in self.visited]

        return (min(x_vals), max(x_vals), min(y_vals), max(y_vals))

    def add_knot(self):
        self.child = RopeKnot(parent=self)
        return self.child

    def check_pos(self):
        print(f'node {self.id} check_pos parent={self.parent.position} self={self.position}')
        xd, yd = [a-b for a, b in zip(self.parent.position, self.position)]
        if abs(xd) <= 1 and abs(yd) <= 1:
            print(f'node {self.id} is close enough to parent, no need to move')
            return
        
        if xd != 0:
            xd = 1 if xd > 0 else -1
        
        if yd != 0:
            yd = 1 if yd > 0 else -1
        
        print(f'node {self.id} is too far away from parent (xd {xd} yd {yd})')
        self.move(xd, yd)

    def move(self, xd, yd):
        print(f'node {self.id} moving {xd},{yd}')
        self.position = [a+b for a, b in zip(self.position, [xd, yd])]

        if self.position not in self.visited:
            self.visited.append(self.position)

        if self.child:
            self.child.check_pos()

class RopeTracker(object):
    dir_map = {
        'U': [0,1],
        'D': [0,-1],
        'L': [-1,0],
        'R': [1,0]        
    }

    def __init__(self, knots=1):
        self.head = RopeKnot()

        parent = self.head
        for _ in range(knots):
            parent = parent.add_knot()

        self.min_x = self.max_x = self.min_y = self.max_y = 0

    def execute_instruction(self, instruction):
        direction, count = instruction.split(' ')
        #print(f'execute direction {direction} count {count}')
        for _ in range(int(count)):
            self.head.move(*RopeTracker.dir_map[direction])

    def print_map(self):
        min_x, max_x, min_y, max_y = self.head.tail().get_field_bounds()
        print(f"field bounds: min_x {min_x} max_x {max_x} min_y {min_y} max_y {max_y}")

        tail = self.head.tail()
        print(f'tail visited {tail.visited}')

        for y in range(max_y, min_y-2, -1):
            line = ''
            for x in range(min_x-2, max_x+2):
                if [x,y] == self.head.position:
                    c = 'H'
                elif [x,y] == tail.position:
                    c = 'T'
                elif x==0 and y==0:
                    c = 's'
                elif [x,y] in tail.visited:
                    c = '#'
                else:
                    c = '.'
                
                line += c
            
            print(line)

def get_data(filename):
    return open(filename, 'rt').read().split('\n')

def solve_part_1(filename):
    rt = RopeTracker()
    for instruction in get_data(filename):
        rt.execute_instruction(instruction)

    rt.print_map()
    tail = rt.head.tail()
    print(f'visited {len(tail.visited)}')

    return len(tail.visited)

def solve_part_2(filename):
    rt = RopeTracker(knots=9)
    for instruction in get_data(filename):
        rt.execute_instruction(instruction)

    rt.print_map()
    tail = rt.head.tail()
    print(f'visited {len(tail.visited)}')

    return len(tail.visited)

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 13:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 5683:
        raise ValueError("Test Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == 1:
        raise ValueError("Tests Failed")


    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 0:
        raise ValueError("Test Failed")