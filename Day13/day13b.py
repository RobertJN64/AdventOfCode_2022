class Result:
    L = "<"
    G = ">"
    E = "="

class SObj:
    def __init__(self, item):
        self.item = item

    def __lt__(self, other):
        return compare(self.item, other.item) == Result.G

    def __repr__(self):
        return str(self.item)


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

    list_to_sort = []
    for i in range(0, len(lines), 3):
        a = eval(lines[i].strip())
        b = eval(lines[i+1].strip())
        list_to_sort.append(SObj(a))
        list_to_sort.append(SObj(b))

    pflag = 1
    for index, item in enumerate(sorted(list_to_sort, reverse=True)):
        print(item)
        if str(item) == "[[6]]":
            pflag *= index + 1
        elif str(item) == "[[2]]":
            pflag *= index + 1
    print(pflag)

