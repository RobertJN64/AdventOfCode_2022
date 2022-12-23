import copy


def pprint(grid):
    print()
    for line in grid:
        print("".join(line))


def strip(grid):
    while "#" not in grid[0]:
        grid.pop(0)
    while "#" not in grid[-1]:
        grid.pop(-1)
    while not any([line[0] == '#' for line in grid]):
        grid = [line[1:] for line in grid]
    while not any([line[-1] == '#' for line in grid]):
        grid = [line[:-1] for line in grid]
    return grid

def border(grid):
    l = len(grid[0])
    grid = [["."] * l] + grid + [["."] * l]
    grid = [["."] + line + ["."] for line in grid]
    return grid

def get_target_movement(grid, x, y, order):
    for dx in [-1, 0, 1]:
        found = False
        for dy in [-1, 0, 1]:
            if (dx != 0 or dy != 0) and grid[y+dy][x+dx] == '#':
                found = True
                break
        if found:
            break
    else:
        return x, y

    for i in range(order, order+4):
        i = i%4
        if i == 0:
            for dx in [-1, 0, 1]:
                if grid[y-1][x+dx] == "#":
                    break
            else:
                return x,y-1
        if i == 1:
            for dx in [-1, 0, 1]:
                if grid[y+1][x+dx] == "#":
                    break
            else:
                return x,y+1
        if i == 2:
            for dy in [-1, 0, 1]:
                if grid[y+dy][x-1] == '#':
                    break
            else:
                return x-1,y
        if i == 3:
            for dy in [-1, 0, 1]:
                if grid[y+dy][x+1] == '#':
                    break
            else:
                return x+1,y



def main():
    with open("Day23/day23.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    order = 0
    for i in range(0, 10):
        grid = strip(grid)
        grid = border(grid)
        pprint(grid)
        archive_grid = copy.deepcopy(grid)



        movement_targets = []
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if grid[y][x] == '#':
                    movement_targets.append(get_target_movement(grid, x, y, order))

        order = (order+1)%4
        mt_counter = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                if archive_grid[y][x] == '#':
                    mt = movement_targets[mt_counter]
                    mt_counter += 1
                    count = 0
                    for item in movement_targets:
                        if mt == item:
                            count += 1
                    if count == 1:
                        grid[y][x] = "."
                        xt, yt = mt
                        grid[yt][xt] = "#"

    grid = strip(grid)
    count = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == '.':
                count += 1
    print(count)