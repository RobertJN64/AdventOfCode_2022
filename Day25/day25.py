import math

vmap = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

def parse_number(line):
    place_value = 5 ** (len(line) - 1)
    val = 0
    for char in line:
        val += place_value * vmap[char]
        place_value /= 5
    return int(val)

def inc(out, index):
    index -= 1
    if index < 0:
        out = ["0"] + out
        index += 1

    if out[index] == "=":
        out[index] = "-"
    elif out[index] == "-":
        out[index] = "0"
    elif out[index] == "0":
        out[index] = "1"
    elif out[index] == "1":
        out[index] = "2"
    elif out[index] == "2":
        out[index] = "="
        out = inc(out, index)
    return out

def reverse_number(x):
    place_val_index = int(math.log(x) / math.log(5))
    out = []
    while place_val_index > -1:
        v = int(x / (5 ** place_val_index))
        out.append(str(v))
        x -= (5 ** place_val_index) * v
        place_val_index -=1

    done = False
    while not done:
        done = True
        for index in range(0, len(out)):
            if out[index] == "3":
                out[index] = "="
                out = inc(out, index)
                done = False
                break
            if out[index] == "4":
                out[index] = "-"
                out = inc(out, index)
                done = False
                break

    return "".join(out)

def main():
    with open("Day25/day25.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    v = sum(parse_number(line) for line in lines)
    print(reverse_number(v))

