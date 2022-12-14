def main():
    with open("Day14/day14.txt") as f:
        lines = f.readlines()

    max_x = 0
    min_x = float('inf')
    max_y = 0
    min_y = 0 #sand level

    t_rock_paths = []
    for line in lines:
        l = line.strip().split(" -> ")
        for index in range(len(l) - 1):
            a = tuple(map(int, l[index].split(",")))
            b = tuple(map(int, l[index+1].split(",")))

            max_x = max(max_x, a[0], b[0])
            min_x = min(min_x, a[0], b[0])
            max_y = max(max_y, a[1], b[1])
            min_y = min(min_y, a[1], b[1])
            t_rock_paths.append((a, b))

    min_x -= 1
    max_x += 1
    max_y += 2

    rock_paths = []
    for ta, tb in t_rock_paths:
        a = (ta[0] - min_x, ta[1] - min_y)
        b = (tb[0] - min_x, tb[1] - min_y)
        rock_paths.append((a, b))

    grid = []
    for row in range(max_y + 1):
        grid.append(["."] * (max_x + 1 - min_x))

    #print(rock_paths)
    for a, b in rock_paths:
        if a[0] == b[0]:
            for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                grid[y][a[0]] = '#'
        else:
            assert a[1] == b[1]
            for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                grid[a[1]][x] = '#'

    for row in grid:
        print(''.join(row))

    print("STARTING SIM")
    done = False
    counter = 0
    while not done:

        sand_pos = (500, 0)
        sand_pos = [sand_pos[0] - min_x, sand_pos[1] - min_y]
        while True:
            if sand_pos[1] >= max_y:
                done = True
                break

            if grid[sand_pos[1] + 1][sand_pos[0]] == '.':
                sand_pos = (sand_pos[0], sand_pos[1] + 1)
            elif grid[sand_pos[1] + 1][sand_pos[0] - 1] == '.':
                sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
            elif grid[sand_pos[1] + 1][sand_pos[0] + 1] == '.':
                sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
            else:
                counter += 1
                grid[sand_pos[1]][sand_pos[0]] = 'o'
                break

    for row in grid:
        print(''.join(row))
    print(counter)



