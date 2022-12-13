class Result:
    L = "<"
    G = ">"
    E = "="

def compare(a, b):
    for ai, bi in zip(a, b):
        if isinstance(ai, list) and isinstance(bi, list):
            r = compare(ai, bi)
            if r != Result.E:
                return r
        elif isinstance(ai, int) and isinstance(bi, int):
            if ai < bi:
                return Result.L
            elif ai > bi:
                return Result.G

        elif isinstance(ai, int) and isinstance(bi, list):
            r = compare([ai], bi)
            if r != Result.E:
                return r
        elif isinstance(ai, list) and isinstance(bi, int):
            r = compare(ai, [bi])
            if r != Result.E:
                return r

    if len(a) > len(b):
        return Result.G
    elif len(a) < len(b):
        return Result.L
    else:
        return Result.E

def main():
    with open("Day13/day13.txt") as f:
        lines = f.readlines()

    score = 0
    for i in range(0, len(lines), 3):
        a = eval(lines[i].strip())
        b = eval(lines[i+1].strip())
        print(a, b, compare(a, b))
        if compare(a, b) == Result.L:
            print("CORRECT")
            score += int((i+3)/3)
        else:
            print("WRONG")

    print(score)
