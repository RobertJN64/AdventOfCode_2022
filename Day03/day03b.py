def prior(x):
    y = ord(x)
    if y > 96:
        y = y - 96
    else:
        y = y - (64-26)
    return y

def main():
    with open("Day03/day03.txt") as f:
        lines = f.readlines()

    s = 0
    for index in range(0, len(lines), 3):
        a = lines[index].strip()
        b = lines[index+1].strip()
        c = lines[index+2].strip()

        s += prior(set(a).intersection(set(b)).intersection(set(c)).pop())
    print(s)
