def main():
    with open("Day09/day09.txt") as f:
        lines = f.readlines()


    head_pos = (0,0)
    tail_pos = (0,0)
    tail_pos_list = {tail_pos}

    print(head_pos)

    for line in lines:
        direction, num = line.strip().split(" ")
        num = int(num)

        for i in range(0, num):
            if direction == "R":
                head_pos = (head_pos[0] + 1, head_pos[1])
            elif direction == "L":
                head_pos = (head_pos[0] - 1, head_pos[1])
            elif direction == "U":
                head_pos = (head_pos[0], head_pos[1] + 1)
            elif direction == "D":
                head_pos = (head_pos[0], head_pos[1] - 1)
            #print(head_pos)

            #CALC TAIL MOVEMENT
            if abs(tail_pos[0] - head_pos[0]) == 2:
                tail_pos = (int((tail_pos[0] + head_pos[0])/2), head_pos[1])

            if abs(tail_pos[1] - head_pos[1]) == 2:
                tail_pos = (head_pos[0], int((tail_pos[1] + head_pos[1])/2))

            print(tail_pos)
            tail_pos_list.add(tail_pos)

    print(len(tail_pos_list))


