def main():
    with open("Day08/day08.txt") as f:
        lines = [line.strip() for line in f.readlines()]


    width = len(lines[0])
    height = len(lines)

    grid = []
    for item in range(0, height):
        grid.append([0] * width)

    for y in range(0, height):
        for x in range(0, width):

            total_score = 1
            base_h = int(lines[y][x])

            t_score = 0
            for xt in range(x - 1, -1, -1):
                h = int(lines[y][xt])
                if h < base_h:
                    t_score += 1
                else:
                    t_score += 1
                    break


            total_score *= t_score

            t_score = 0
            for xt in range(x + 1, width):
                h = int(lines[y][xt])
                if h < base_h:
                    t_score += 1
                else:
                    t_score += 1
                    break

            total_score *= t_score

            t_score = 0
            for yt in range(y - 1, -1, -1):
                h = int(lines[yt][x])
                if h < base_h:
                    t_score += 1
                else:
                    t_score += 1
                    break

            total_score *= t_score

            t_score = 0
            for yt in range(y + 1, height):
                h = int(lines[yt][x])
                if h < base_h:
                    t_score += 1
                else:
                    t_score += 1
                    break

            total_score *= t_score




            grid[y][x] = total_score




    m = 0
    for row in grid:
        m = max(max(row), m)
        print(row)

    print(m)
