import copy


def check_in_range(scan_index, a, b):
    return min(a, b) <= scan_index <= max(a, b)

def print_order(data: list[tuple]):
    d = copy.deepcopy(data)
    d.sort(key=lambda x:x[1])
    print(', '.join([str(x[0]) for x in d]))

def get_index(data, index):
    start = 0
    for val, sindex in data:
        if val == 0:
            start = sindex
    start += index
    start = start%len(data)

    for val, ind in data:
        if ind == start:
            return val

def integrity_check(data):
    for _, ind in data:
        if 0 > ind or ind > len(data):
            print(ind)
            print(data)
            quit()

def super_mod(val, ld):
    """
    equiv to
    while val <= 0:
        val += (ld-1)

    while val >= ld:
        val -= (ld-1)
    """

    if val < 0:
        val = abs(val)
        val = val%(ld-1)
        val = -val + (ld-1)
        return val

    else:
        val = val % (ld - 1)
        return val

def int_mul(x):
    return int(x) * 811589153

def main():
    with open("Day20/day20.txt") as f:
        lines = f.readlines()

    data = list(zip(map(int_mul, lines), range(0, len(lines))))

    for i in range(0, 10):
        print(i)
        for rindex in range(0, len(data)):
            val, start_index = data[rindex]

            end_index = start_index + val
            ld = len(data)
            true_end_index = end_index
            true_end_index = super_mod(true_end_index, ld)

            data[rindex] = (val, true_end_index)

            #print(val, start_index, true_end_index)

            for sindex in range(0, len(data)):
                if check_in_range(data[sindex][1], start_index, true_end_index) and sindex != rindex:
                    if true_end_index < start_index:
                        data[sindex] = (data[sindex][0], data[sindex][1] + 1)
                    elif true_end_index > start_index:
                        data[sindex] = (data[sindex][0], data[sindex][1] - 1)

            integrity_check(data)
            #print_order(data)
    print(get_index(data, 1000) + get_index(data, 2000) + get_index(data, 3000))



