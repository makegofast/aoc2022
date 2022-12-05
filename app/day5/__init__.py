import re

class Solver(object):
    @staticmethod
    def get_data(filename):
        columns = {} 
        moves = []

        data = open(filename, 'rt').read()
        field_data, move_data = data.split('\n\n')

        field_lines = field_data.split('\n')[:-1]
        for field_line in field_lines:
            row = [field_line[i+1:i+2] for i in range(0, len(field_line), 4)]
            for col, val in enumerate(row):
                columns.setdefault(col+1, [])
                if val.strip():
                    columns[col+1].insert(0, val)

        for move_line in move_data.split('\n'):
            nums = re.findall(r'\d+', move_line)
            moves.append({
                'count': int(nums[0]),
                'from': int(nums[1]),
                'to': int(nums[2])
            })
        
        return (columns, moves)

    def solve_part_1(self, filename):
        columns, moves = Solver.get_data(filename)
        for move in moves:
            for _ in range(move['count']):
                val = columns[move['from']].pop()
                columns[move['to']].append(val)

        tops = ''.join([s[-1] for s in columns.values()])
        print(f'part 1 final: {tops}')
        return tops

    def solve_part_2(self, filename):
        columns, moves = Solver.get_data(filename)
        
        for move in moves:
            accum = []
            for _ in range(move['count']):
                accum.insert(0, columns[move['from']].pop())
            columns[move['to']] += accum

        tops = ''.join([s[-1] for s in columns.values()])
        print(f'part 2 final: {tops}')
        return tops

if __name__ == "__main__":
    solver = Solver()
    if not solver.solve_part_1('test_data.txt') == 'CMZ':
        raise ValueError("Tests Failed")

    solver = Solver()
    if not solver.solve_part_1('data.txt') == 'FRDSQRRCD':
        raise ValueError("Test Failed")

    solver = Solver()
    if not solver.solve_part_2('test_data.txt') == 'MCD':
        raise ValueError("Tests Failed")

    solver = Solver()
    if not solver.solve_part_2('data.txt') == 'HRFTQVWNN':
        raise ValueError("Test Failed")