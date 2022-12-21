import copy

def main():
    with open("Day21/day21.txt") as f:
        lines = [line.strip().replace(":", " =") for line in f.readlines()]

    r = copy.copy(lines)
    while r:
        l = copy.copy(r)
        r = []
        for line in l:
            try:
                exec(line)
            except:
                print(line)
                r.append(line)

    exec("print(root)")
