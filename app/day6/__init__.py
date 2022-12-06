def solve(filename, window_size):
    data = open(filename, 'rt').read()
    for i in range(window_size, len(data)):
        if len(set(data[i-window_size:i])) == window_size:
            print(f'{window_size} position: {i}')
            return i

if not all([
    solve('test_data.txt', 4) == 7,
    solve('data.txt', 4) == 1287,
    solve('test_data.txt', 14) == 19,
    solve('data.txt', 14) == 3716
]):
    raise ValueError("Test Failed")