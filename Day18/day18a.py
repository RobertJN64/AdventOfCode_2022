import copy


def main():
    with open("Day18/day18.txt") as f:
        lines = f.readlines()

    data = []
    for line in lines:
        data.append(list(map(int, line.split(","))))
    print(data)

    SA = 0
    for point in data:
        for index in range(len(point)):
            for d in [-1, 1]:
                p = copy.copy(point)
                p[index] += d

                for p2 in data:
                    if p[0] == p2[0] and p[1] == p2[1] and p[2] == p2[2]:
                        break
                else:
                    SA += 1

    print(SA)