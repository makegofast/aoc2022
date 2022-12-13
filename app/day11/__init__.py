import numpy
import math

class Item(object):
    def __init__(self, start):
        print(f'created new item with {start}')
        self.value = start
        self.primes = [2,3,5,7,11,13,17,19]
        #self.primes = [23,19,13,17]
        self.values = {p: start for p in self.primes}

    def __floordiv__(self, divisor):
        self.value //= divisor
        return self

    def __mod__(self, other):
        return self.value % other

    def __int__(self):
        return self.value
    
    def add_operation(self, operation, use_part_2):
        if use_part_2:
            for p in self.primes:
                if self.values[p] <= 0:
                    raise ValueError(f'wtf {self.values[p]} {p}')

                self.values[p] = self.apply_operation(self.values[p], operation, p)
        else:
            self.value = self.apply_operation(self.value, operation)
    
    def apply_operation(self, old, operation, reduce=None):
        if old <= 0:
            raise ValueError(f'wtf2 {old}')
        #print(f'apply_operation {reduce} {operation} to {old}')
        _, operator, value = operation
        value = int(value) if value.isnumeric() else value

        if reduce and operator == '*' and old % reduce == 0:
            old = reduce

        if operator == '*' and value == 'old':
            new = old**2
        elif operator == '+':
            new = old + value
        elif operator == '*':
            new = old * value
        
        return new

    def is_divisible_by(self, divisor, part_2_rules):
        return self.values[divisor] % divisor == 0 if part_2_rules else self.value % divisor == 0
    
    def __str__(self):
        return f'Item({self.value})'
    
class Monkey(object):
    def __init__(self, monkey_data, parent):
        self.test_cache = {} 

        self.parent = parent
        monkey_data = [line.strip().split(': ') for line in monkey_data]
        self.inspections = 0

        self.id = monkey_data.pop(0)[0][-2:-1]

        for field, value in monkey_data:
            setattr(self, field.lower().split()[-1], value)

        self.items = [Item(int(value)) for value in self.items.split(', ')]
        self.operation = self.operation.split(' = ')[-1].split()
        self.test = int(self.test.split()[-1])
        self.true = int(self.true.split()[-1])
        self.false = int(self.false.split()[-1])

        #print(f'🐒 {self.id}: items={self.items}, operation={self.operation}, test={self.test}, true={self.true}, false={self.false}')
    
    def inspect_items(self, part_2_rules):
        #print(f'🐒 {self.id} inspecting...')
        for _ in range(len(self.items)):
            item = self.items.pop(0)
            item.add_operation(self.operation, part_2_rules)
            #print(f'🐒{self.id} check if {item} is divisible by {self.test}')
            
            if not part_2_rules:
                item = item//3

            if item.is_divisible_by(self.test, part_2_rules):
                target_monkey = self.true
            else:
                target_monkey = self.false

            self.inspections += 1
            #print(f' old = {old}, operation={self.operation}, test={self.test}, new={new}, concern={concern}, inspections={self.inspections}')
            #print(f'🐒 {self.id} {self.operation} throwing {item} to {target_monkey}')
            self.parent.handle_throw(item, target_monkey)
    
    def catch(self, item):
        #print(f'🐒 {self.id} caught item {item}')
        self.items.append(item)

class MonkeyBusiness(object):
    def __init__(self, monkey_input):
        self.monkies = []

        for monkey_data in monkey_input: 
            self.monkies.append(Monkey(monkey_data.split('\n'), parent=self))
        
        self.primes = [m.test for m in self.monkies]

    def play_rounds(self, count, part_2_rules):
        for round in range(1, count+1):
            #print(f'Round {round}')
            self.play_round(part_2_rules)

            if round in [1, 20, 1000, 2000, 3000, 10000]:
                print(f'== After round {round} ==')
                for line in [f'Monkey {m.id} inspected items {m.inspections} times' for m in self.monkies]:
                    print(line)

        return math.prod(sorted([monkey.inspections for monkey in self.monkies], reverse=True)[0:2])

    def play_round(self, part_2_rules):
        for monkey in self.monkies:
            monkey.inspect_items(part_2_rules)
    
    def handle_throw(self, item, target):
        self.monkies[target].catch(item)

def get_data(filename):
    return open(filename, 'rt').read().split('\n\n')

def solve_part_1(filename):
    mb = MonkeyBusiness(get_data(filename))
    monkey_business = mb.play_rounds(20, part_2_rules=False)

    print(f'part 1 monkey business = {monkey_business}')
    return monkey_business

def solve_part_2(filename):
    mb = MonkeyBusiness(get_data(filename))
    monkey_business = mb.play_rounds(10000, part_2_rules=True)

    print(f'part 2 monkey business = {monkey_business}')
    return monkey_business

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 10605:
        raise ValueError("Part 1 Test Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 57348:
        raise ValueError("Part 1 Failed")

    #print("Running Test Part 2...")
    #if not solve_part_2('test_data.txt') == 2713310158:
    #   raise ValueError("Part 2 Test Failed")

    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 14106266886:
        raise ValueError("Part 2 Failed")