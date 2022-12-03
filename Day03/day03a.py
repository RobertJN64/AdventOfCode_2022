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
    for line in lines:
        line = line.strip()
        a = line[:int(len(line)/2)]
        b = line[int(len(line)/2):]
        a = set(a)
        b = set(b)
        s += (prior(a.intersection(b).pop()))

    print(s)

