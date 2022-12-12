def main():
    with open("Day12/day12.txt") as f:
        lines = f.readlines()

    start_pos = (0,0)
    end_pos = (0,0)
    grid = []
    costs = []

    for index, line in enumerate(lines):
        grid.append(list(map(ord, line.strip().replace("S", "a").replace("E", "z"))))
        costs.append([float('inf')] * len(grid[0]))
        if "S" in line:
            start_pos = (line.index("S"), index)
        if "E" in line:
            end_pos = (line.index("E"), index)

    print(start_pos)
    print(end_pos)
    costs[end_pos[1]][end_pos[0]] = 0

    changed = True
    while changed:
        changed = False
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    n_x = x + dx
                    n_y = y + dy
                    if 0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid):
                        if costs[n_y][n_x] + 1 < costs[y][x]:
                            if grid[n_y][n_x] - grid[y][x] <= 1:
                                costs[y][x] = costs[n_y][n_x] + 1
                                changed = True
    print(costs[start_pos[1]][start_pos[0]])



if __name__ == '__main__':
    main()