def main():
    with open("Day18/day18.txt") as f:
        lines = f.readlines()

    data = []
    for line in lines:
        data.append(tuple(map(int, line.split(","))))
    print(data)

    min_x = min(p[0] for p in data) - 1
    min_y = min(p[1] for p in data) - 1
    min_z = min(p[2] for p in data) - 1

    max_x = max(p[0] for p in data) + 2
    max_y = max(p[1] for p in data) + 2
    max_z = max(p[2] for p in data) + 2

    db = []
    for z in range(min_z, max_z):
        db_grid = []
        for y in range(min_y, max_y):
            db_row = []
            for x in range(min_x, max_x):
                db_row.append('.')
            db_grid.append(db_row)
        db.append(db_grid)

    for point in data:
        x, y, z = point
        x -= min_x
        y -= min_y
        z -= min_z
        db[z][y][x] = '*'

    db[0][0][0] = 'A'
    done = False
    while not done:
        done = True
        for z in range(0, len(db)):
            for y in range(0, len(db[0])):
                for x in range(0, len(db[0][0])):
                    if db[z][y][x] == '.':
                        for dz in [-1, 1]:
                            try:
                                if db[z + dz][y][x] == 'A':
                                    db[z][y][x] = 'A'
                                    done = False
                            except IndexError:
                                pass

                        for dy in [-1, 1]:
                            try:
                                if db[z][y + dy][x] == 'A':
                                    db[z][y][x] = 'A'
                                    done = False
                            except IndexError:
                                pass

                        for dx in [-1, 1]:
                            try:
                                if db[z][y][x + dx] == 'A':
                                    db[z][y][x] = 'A'
                                    done = False
                            except IndexError:
                                pass

    for grid in db:
        print('-')
        for row in grid:
            print(''.join(row))

    for z in range(0, len(db)):
        for y in range(0, len(db[0])):
            for x in range(0, len(db[0][0])):
                if db[z][y][x] == '.':
                    print(x + min_x, y + min_y, z + min_z, sep=',')

    #METHOD 2
    SA = 0
    for z in range(0, len(db)):
        for y in range(0, len(db[0])):
            for x in range(0, len(db[0][0])):
                if db[z][y][x] == '*':
                    for d in [-1, 1]:
                        if db[z + d][y][x] == 'A':
                            SA += 1
                    for d in [-1, 1]:
                        if db[z][y + d][x] == 'A':
                            SA += 1
                    for d in [-1, 1]:
                        if db[z][y][x + d] == 'A':
                            SA += 1
    print(SA)
