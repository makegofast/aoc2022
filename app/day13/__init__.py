import math
import json

class PacketParser(object):
    def __init__(self, packet):
        self.packet = packet 
    
    def __eq__(self, other):
        return self.compare(self.packet, other.packet) == None
    
    def __lt__(self, other):
        return self.compare(self.packet, other.packet) == True

    def __str__(self):
        return f'ParserPacket({self.packet})'

    def compare(self, a, b):
        #print(f'  comparing {a} {type(a)} to {b} {type(b)}')

        if type(a) != type(b):
            #print(f'  mixed comparision between {a} {type(a)} and {b} {type(b)}')
            a = a if isinstance(a, list) else [a]
            b = b if isinstance(b, list) else [b]
            #print(f'  updated {a} and {b}')

        if isinstance(a, int) and isinstance(b, int):
            #print(f'  comparing int {a} to int {b}')
            if a < b:
                #print(f'  {a} < {b} = True')
                return True
            elif a > b:
                #print(f'  {a} > {b} = False')
                return False

            return None
        elif isinstance(a, list) and isinstance(b, list):
            for left, right in zip(a, b):
                #print(f'  recursing into {left} ? {right}')
                result = self.compare(left, right)

                if result == None:
                    continue
                else:
                    return result
            
            if len(a) == len(b):
                return None
            else:
                return True if len(a) < len(b) else False
        
def get_data(filename):
    data = open(filename, 'rt').read()

    return [pair.split('\n') for pair in data.split('\n\n')]

def solve_part_1(filename):
    data = get_data(filename)

    results = []
    count = 0
    for packet_a, packet_b in data:
        count += 1
        print(f'#{count} Testing {packet_a} to {packet_b}')
        if PacketParser(json.loads(packet_a)) < PacketParser(json.loads(packet_b)):
            results.append(count)
    
    print(results)
    print(f'part 1 result: {sum(results)}')
    return sum(results)

def solve_part_2(filename):
    data = get_data(filename)

    decoder_packets = [PacketParser([[2]]), PacketParser([[6]])]
    packets = decoder_packets

    for a, b in data:
        packets.append(PacketParser(json.loads(a)))
        packets.append(PacketParser(json.loads(b)))

    sorted_packets = sorted(packets)
    #print('\n'.join([str(p) for p in sorted_packets]))
    for i, p in enumerate(sorted_packets):
        print(p, p == decoder_packets[0] or p == decoder_packets[1])

    decoder_key = math.prod([i+1 for i, p in enumerate(sorted_packets) if p == decoder_packets[0] or p == decoder_packets[1]])
    print(f'Decoder key = {decoder_key}')
    return decoder_key

if __name__ == "__main__":
    print("Running Test Part 1...")
    if not solve_part_1('test_data.txt') == 13:
        raise ValueError("Part 1 Tests Failed")

    print("Solving Part 1...")
    if not solve_part_1('data.txt') == 5330:
        raise ValueError("Part 1 Failed")

    print("Running Test Part 2...")
    if not solve_part_2('test_data.txt') == 140:
        raise ValueError("Part 2 Tests Failed")

    print("Solving Part 2...")
    if not solve_part_2('data.txt') == 27648:
        raise ValueError("Part 2 Failed")