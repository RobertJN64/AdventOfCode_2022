import math

vmap = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

def parse_number(line):
    place_value = 5 ** (len(line) - 1)
    val = 0
    for char in line:
        val += place_value * vmap[char]
        place_value /= 5
    return int(val)

def reverse_number(x):
    place_ind = math.floor(math.log(x) / math.log(5))
    out = ""
    while x != 0:
        pval = 5 ** place_ind
        v = x / pval

        if v >= 4:
            out += "2"
            x -= 10 * pval

        elif v >= 3:
            out += "1"
            x -= 5 * pval

        elif v >= 2:
            out += "2"
            x -= 2 * pval

        elif v >= 1:
            out += "1"
            x -= pval

        elif v <= -2:
            out += "="
            x += pval * 2

        elif v <= -1:
            out += "-"
            x += pval

    return out


def main():
    with open("Day25/day25.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        print(parse_number(line))

    v = sum(parse_number(line) for line in lines)
    print("Rev num")
    #print("r", reverse_number(1))
    #print("r", reverse_number(2))
    #print("r", reverse_number(3))
    print("r", reverse_number(4))
    #print("r", reverse_number(5))

