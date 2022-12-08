

def main():
    with open("Day08/day08.txt") as f:
        lines = [line.strip() for line in f.readlines()]


    width = len(lines[0])
    height = len(lines)

    grid = []
    for item in range(0, height):
        grid.append([False] * width)


    for y in range(0, height):
        maxh = -1
        for x in range(0, width):
            h = int(lines[y][x])
            if h > maxh:
                grid[y][x] = True
            maxh = max(maxh, h)

        maxh = -1
        for x in range(width - 1, -1, -1):
            h = int(lines[y][x])
            if h > maxh:
                grid[y][x] = True
            maxh = max(maxh, h)

    for x in range(0, width):
        maxh = -1
        for y in range(0, height):
            h = int(lines[y][x])
            if h > maxh:
                if x == 3 and y == 3:
                    print("a")
                grid[y][x] = True
            maxh = max(maxh, h)

        maxh = -1
        for y in range(height - 1, -1, -1):
            h = int(lines[y][x])
            if h > maxh:

                grid[y][x] = True
            maxh = max(maxh, h)


    count = 0
    for row in grid:
        for item in row:
            if item:
                 count += 1
        print(row)

    print(count)
