def main():
    with open("Day09/day09.txt") as f:
        lines = f.readlines()

    pos_list = [(0,0) for _ in range(0, 10)]
    tail_pos_list = {pos_list[9]}


    for line in lines:
        direction, num = line.strip().split(" ")
        num = int(num)

        for i in range(0, num):
            if direction == "R":
                pos_list[0] = (pos_list[0][0] + 1, pos_list[0][1])
            elif direction == "L":
                pos_list[0] = (pos_list[0][0] - 1, pos_list[0][1])
            elif direction == "U":
                pos_list[0] = (pos_list[0][0], pos_list[0][1] + 1)
            elif direction == "D":
                pos_list[0] = (pos_list[0][0], pos_list[0][1] - 1)


            #CALC TAIL MOVEMENT
            for tp in range(1, 10):
                if abs(pos_list[tp][0] - pos_list[tp-1][0]) == 2 and abs(pos_list[tp][1] - pos_list[tp - 1][1]) == 2:
                    pos_list[tp] = (int((pos_list[tp][0] + pos_list[tp - 1][0]) / 2),
                                    int((pos_list[tp][1] + pos_list[tp - 1][1]) / 2))

                elif abs(pos_list[tp][0] - pos_list[tp-1][0]) == 2:
                    pos_list[tp] = (int((pos_list[tp][0] + pos_list[tp-1][0])/2), pos_list[tp-1][1])

                elif abs(pos_list[tp][1] - pos_list[tp - 1][1]) == 2:
                    pos_list[tp] = (pos_list[tp - 1][0], int((pos_list[tp][1] + pos_list[tp - 1][1]) / 2))

            #print(pos_list[9])
            tail_pos_list.add(pos_list[9])

    print(len(tail_pos_list))

    # grid = []
    # for i in range(0, 1000):
    #     row = ['.'] * 1000
    #     grid.append(row)
    #
    # for item in tail_pos_list:
    #     grid[int(-item[1] - len(grid)/2)][int(item[0] + len(grid)/2)] = '#'
    #
    # for row in grid:
    #     print(''.join(row))


