import copy


def main():
    with open("Day18/day18.txt") as f:
        lines = f.readlines()

    data = []
    for line in lines:
        data.append(tuple(map(int, line.split(","))))
    print(data)

    #STEP 1: CLUMP!
    clumps: list[set[tuple]] = []

    for point in data:
        clump = set()
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                for dz in [-1,0,1]:
                    p = list(copy.copy(point))
                    p[0] += dx
                    p[1] += dy
                    p[2] += dz

                    for p2 in data:
                        if p[0] == p2[0] and p[1] == p2[1] and p[2] == p2[2]:
                            clump.add(p2)
        clumps.append(clump)


    for point in data:
        active_clumps = []

        for clump in clumps:
            if point in clump:
                active_clumps.append(clump)

        new_clump = set()
        for clump in active_clumps:
            new_clump = new_clump.union(clump)
            clumps.remove(clump)
        clumps.append(new_clump)

    for c in clumps:
        print(c)

    SA = 0
    print(len(clumps))
    for clump in clumps:
        print(clump)
        min_x = min(p[0] for p in clump) - 1
        min_y = min(p[1] for p in clump) - 1
        min_z = min(p[2] for p in clump) - 1

        max_x = max(p[0] for p in clump) + 2
        max_y = max(p[1] for p in clump) + 2
        max_z = max(p[2] for p in clump) + 2

        db = []
        for z in range(min_z, max_z):
            db_grid = []
            for y in range(min_y, max_y):
                db_row = []
                for x in range(min_x, max_x):
                    db_row.append('.')
                db_grid.append(db_row)
            db.append(db_grid)

        for point in clump:
            x, y, z = point
            x -= min_x
            y -= min_y
            z -= min_z
            db[z][y][x] = '*'

        # try:
        #     #db[5 - min_z][2 - min_y][2 - min_x] = '&'
        # except:
        #     pass


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
        for z in range(0, len(db)):
            for y in range(0, len(db[0])):
                for x in range(0, len(db[0][0])):
                    if db[z][y][x] == '.':
                        print(x + min_x, y + min_y, z + min_z, sep=',')

