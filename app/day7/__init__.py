class DirTracker(object):
    def __init__(self):
        self._dirtree = {'_path': [], '_files': {}}
        self._cwdptr = self._dirtree 

    def parse_line(self, line: str):
        if line.startswith('$'):
            parts = line[2:].split(' ', 1)
            cmd = parts.pop(0)
            arg = parts.pop(0) if len(parts) else None

            func_name = f'_handle_cmd_{cmd}' 
            if hasattr(self, func_name):
                func = getattr(self, func_name)
                func(arg)
        else:
            self._handle_output(line.split(' '))
    
    def _handle_output(self, args):
        if args[0] == 'dir':
            pass
        elif args[0].isdigit():
            size, filename = args
            self._cwdptr['_files'][filename] = int(size)
        else:
            raise ValueError(f"Don't know how to handle f{args}")

    def _handle_cmd_cd(self, arg: str):
        if arg == '/':
            self._cwdptr = self._dirtree
        elif arg == '..':
            self._cwdptr = self._cwdptr['_parent']
        else:
            self._cwdptr.setdefault(arg, {'_path': self._cwdptr['_path'] + [arg], '_parent': self._cwdptr, '_files': {}})
            self._cwdptr = self._cwdptr[arg]
    
    def _calc_dir_usage(self, root):
        matches = {} 
        size = sum(root['_files'].values())

        for k, v in root.items():
            if k.startswith('_'):
                continue

            sub_size, sub_matches = self._calc_dir_usage(root[k])
            size += sub_size

            if sub_matches:
                matches.update(sub_matches)

            matches.update({'/'.join(root[k]['_path']): sub_size})

        return size, matches
    
    def _handle_cmd_ls(self, arg):
        pass
    
    def _parse_output(self, line: str):
        pass

def get_data(filename):
    return open(filename, 'rt').read().split('\n')

def solve_part_1(filename):
    dt = DirTracker()
    for line in get_data(filename):
        dt.parse_line(line)
    
    size, matches = dt._calc_dir_usage(dt._dirtree)
    sum_matches = sum([v for k, v in matches.items() if v <= 100000])
    print(f'part 1: total size {size}, sum matches {sum_matches}')

    return sum_matches

def solve_part_2(filename):
    fs_size = 70000000
    fs_required = 30000000

    dt = DirTracker()
    for line in get_data(filename):
        dt.parse_line(line)
    
    used_space, matches = dt._calc_dir_usage(dt._dirtree)

    free_space = fs_size - used_space
    needed_space = fs_required - free_space

    short_straw = sorted([v for k, v in matches.items() if v >= needed_space])[0]
    print(f'part 2: short straw {short_straw}')

    return short_straw

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 95437:
        raise ValueError("Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 2104783:
        raise ValueError("Test Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == 24933642:
        raise ValueError("Tests Failed")


    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 5883165:
        raise ValueError("Test Failed")