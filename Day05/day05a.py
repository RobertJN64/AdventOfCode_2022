def main():
    with open("Day05/day05pic.txt") as f:
        lines = f.readlines()

    lcount = len(lines[-1].strip().split("   "))
    cols = []
    for item in range(0, lcount):
        cols.append([])

    lines = lines[:-1]
    lines.reverse()

    for line in lines:
        line = line.removesuffix('\n')
        for gindex in range(0, len(line), 4):
            if line[gindex+1:gindex+2] != " ":
                cols[int(gindex/4)].append(line[gindex+1:gindex+2])

    with open("Day05/day05.txt") as f:
        lines = f.readlines()

    for line in lines:
        cmds = line.split()
        count = int(cmds[1])
        start = int(cmds[3]) - 1
        end = int(cmds[5]) - 1

        for i in range(0, count):
            cols[end].append(cols[start].pop())

    for item in cols:
        print(item[-1], end='')