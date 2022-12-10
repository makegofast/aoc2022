import random

class ElfCPU(object):
    pixel_choices = '🔴🟠🟡🟢🔵🟣'

    def __init__(self):
        self.signal_strengths = []
        self.cycle = 0
        self.x = 1
        self.y = 0
        self.screen = [[] for _ in range(0,6)]

    def gen_divider(self):
        return ''.join(['️🎄' for _ in range(0,40)])
            
    def print_screen(self):
        print()
        
        print(self.gen_divider() + f' cycle {self.cycle} x={self.x} y={self.y}')
        for row in self.screen:
            print(''.join(row))
        print(self.gen_divider())

        print()

    def tick(self):
        self.screen[self.y].append(random.choice(ElfCPU.pixel_choices[self.y]) if self.cycle%40 in range(self.x-1, self.x+2) else '⚫️')

        self.cycle += 1

        if self.cycle % 40 == 0:
            self.y += 1

        if (self.cycle - 20) % 40 == 0:
            self.signal_strengths.append(self.x * self.cycle)
        
    def execute_code(self, code):
        for line in code: 
            parts = line.split()
            instruction = parts.pop(0)
            argument = parts.pop(0) if parts else None

            func = getattr(self, f'_exec_{instruction}')
            func(argument)
        
    def _exec_noop(self, argument):
        self.tick()

    def _exec_addx(self, argument):
        self.tick()
        self.tick()
        self.x += int(argument)

def get_data(filename):
    return open(filename, 'rt').read().splitlines()

def solve_part_1(filename):
    code = get_data(filename)
    ecpu = ElfCPU()
    ecpu.execute_code(code)

    sum_signal_strengths = sum(ecpu.signal_strengths)
    print(f'signal strengths {ecpu.signal_strengths} sum={sum_signal_strengths}')

    return sum_signal_strengths

def solve_part_2(filename):
    code = get_data(filename)
    ecpu = ElfCPU()
    ecpu.execute_code(code)
    ecpu.print_screen()

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 13140:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 15260:
        raise ValueError("Test Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == None:
        raise ValueError("Tests Failed")

    print("Solving Part 2...")
    if not solve_part_2('data.txt') == None:
        raise ValueError("Test Failed")