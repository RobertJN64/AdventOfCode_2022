min_x = 0
min_y = 0
max_x = 0
max_y = 0

def compute_bliz_locs(blizzard_list):
    retval = []
    for bliz in blizzard_list:
        if bliz[2] == 0:
            bliz = (bliz[0] + 1, bliz[1], bliz[2])
            if bliz[0] > max_x:
                bliz = (min_x, bliz[1], bliz[2])
            retval.append(bliz)

        elif bliz[2] == 2:
            bliz = (bliz[0] - 1, bliz[1], bliz[2])
            if bliz[0] < min_x:
                bliz = (max_x, bliz[1], bliz[2])
            retval.append(bliz)

        elif bliz[2] == 1:
            bliz = (bliz[0], bliz[1] + 1, bliz[2])
            if bliz[1] > max_y:
                bliz = (bliz[0], min_y, bliz[2])
            retval.append(bliz)


        elif bliz[2] == 3:
            bliz = (bliz[0], bliz[1] - 1, bliz[2])
            if bliz[1] < min_y:
                bliz = (bliz[0],  max_y, bliz[2])
            retval.append(bliz)

        else:
            raise Exception(f"INVALID BILZ: ", bliz)

    return retval

def compute_time(bliz_db, start_pos, start_time, end_pos):
    reached_list = []

    # QUEUE ITEM: (pos, blizard_locs)
    queue = [(start_pos, start_time)]  # START AT TIME 0
    counter = 0

    while queue:
        pos, time = queue.pop(0)

        while time >= len(reached_list):
            reached_list.append([])
        if pos in reached_list[time]:
            continue
        else:
            reached_list[time].append(pos)

        if counter%1000 == 0:
            print(counter, time, len(queue))
        counter += 1
        if (time+1) >= len(bliz_db):
            bliz_db.append(compute_bliz_locs(bliz_db[time]))

        bliz_list = bliz_db[time+1]
        for dx, dy in [(0,0), (1,0), (0,1), (-1,0), (0,-1)]:
            x = pos[0] + dx
            y = pos[1] + dy

            if (x, y) == end_pos:
                return time+1

            if (x, y) != start_pos and (x < min_x or x > max_x or y < min_y or y > max_y):
                continue

            found = False
            for item in bliz_list:
                if item[0] == x and item[1] == y:
                    found = True
                    break
            if found:
                continue

            queue.append(((x,y), time+1))



def main():
    global min_x, min_y, max_x, max_y
    with open("Day24/day24.txt") as f:
        grid = [line.strip() for line in f.readlines()]

    start_pos = (grid[0].index("."), 0)
    end_pos = (grid[-1].index("."), len(grid)-1)

    min_x = 1
    min_y = 1
    max_x = len(grid[0]) - 2
    max_y = len(grid) - 2

    #BLIZZARD = list(X, Y, FACING); FACING: 0: RIGHT, 1: DOWN, 2: LEFT, 3: UP
    blizzard_list = []

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == '>':
                blizzard_list.append((x, y, 0))
            elif grid[y][x] == 'v':
                blizzard_list.append((x, y, 1))
            elif grid[y][x] == '<':
                blizzard_list.append((x, y, 2))
            elif grid[y][x] == '^':
                blizzard_list.append((x, y, 3))

    bliz_db = [blizzard_list]
    a = compute_time(bliz_db, start_pos, 0, end_pos)
    print("SOLUTION: ", a)