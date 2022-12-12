def main():
    with open("Day12/day12.txt") as f:
        lines = f.readlines()
    end_pos = (0,0)
    grid = []
    costs = []

    for index, line in enumerate(lines):
        grid.append(list(map(ord, line.strip().replace("S", "a").replace("E", "z"))))
        costs.append([float('inf')] * len(grid[0]))
        if "E" in line:
            end_pos = (line.index("E"), index)

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

    best_cost = float('inf')
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == ord('a'):
                best_cost = min(best_cost, costs[y][x])
    print(best_cost)


if __name__ == '__main__':
    main()