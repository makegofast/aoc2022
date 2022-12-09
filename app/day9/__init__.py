class RopeKnot(object):
    def __init__(self, parent):
        self.loc = [0,0]
        self.head = None
        self.tail = None
    
    #def attach_tail(self, ) 

class RopeTracker(object):
    dir_map = {
        'U': [0,1],
        'D': [0,-1],
        'L': [-1,0],
        'R': [1,0]        
    }

    def __init__(self):
        self.head = [0,0]
        self.tail = [0,0]

        self.tail_visited = set()
        self.min_x = self.max_x = self.min_y = self.max_y = 0
    
    def move_tail(self):
        xd, yd = [a-b for a, b in zip(self.head, self.tail)]

        #print(f'head {self.head} tail {self.tail} xd {xd} yd {yd}')

        if abs(xd) <= 1 and abs(yd) <= 1:
            #print('tail is close enough to head, no move')
            return
        
        if xd != 0:
            xd = 1 if xd > 0 else -1
        
        if yd != 0:
            yd = 1 if yd > 0 else -1

        #print(f'need to move tail {xd}, {yd}')
        
        self.tail = [a+b for a, b in zip(self.tail, [xd, yd])]

    def execute(self, instruction):
        direction, count = instruction.split(' ')
        #print(f'execute direction {direction} count {count}')
        for _ in range(int(count)):
            #print(f'move head {direction}')
            self.head = [a+b for a, b in zip(self.head, RopeTracker.dir_map[direction])]

            self.move_tail()
            self.tail_visited.add(str(self.tail))

            self.min_x, self.min_y = (min(self.min_x, self.head[0], self.tail[0]), min(self.min_y,self.head[1], self.tail[1]))
            self.max_x, self.max_y = (max(self.max_x, self.head[0], self.tail[0]), max(self.max_y,self.head[1], self.tail[1]))

            #print(f'loc head {self.head} loc tail {self.tail}')
            #self.print_map()

    def print_map(self):
        for y in range(self.max_y, self.min_y-1 , -1):
            line = ''
            for x in range(self.min_x, self.max_x+1):
                if [x,y] == self.head:
                    c = 'H'
                elif [x,y] == self.tail:
                    c = 'T'
                elif x==0 and y==0:
                    c = 's'
                elif str([x,y]) in self.tail_visited:
                    c = '#'
                else:
                    c = '.'
                
                line += c

def get_data(filename):
    return open(filename, 'rt').read().split('\n')

def solve_part_1(filename):
    rt = RopeTracker()
    for instruction in get_data(filename):
        rt.execute(instruction)

    rt.print_map()
    print(f'visited {len(rt.tail_visited)}')

    return len(rt.tail_visited)

def solve_part_2(filename):
    pass

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 13:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 5683:
        raise ValueError("Test Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == 0:
        raise ValueError("Tests Failed")


    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 0:
        raise ValueError("Test Failed")