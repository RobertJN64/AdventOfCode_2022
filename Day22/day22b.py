CUBE_SIZE = 4

def check_wall(maze, pos):
    return maze[pos[1]][pos[0]] == '#'

def in_range(x, interval):
    return CUBE_SIZE * interval <= x <= CUBE_SIZE * (interval + 1)

def calc_wrap(maze, pos, facing): #rewrite to handle cube physics
    x, y = pos
    if maze[y][x] != ' ':
        return x, y

    if facing == 3: #UP
        if in_range(x, 2):
            y -= CUBE_SIZE * 3 #WRAP FROM
            y += 1

    return x, y


def main():
    with open("Day22/day22.txt") as f:
        lines = f.readlines()

    cmd_str = lines[-1].strip().replace("L", "L ").replace("R", "R ") + "X" #X is null cmd
    cmds = cmd_str.split(" ")
    cmds = [(int(num[:-1]), num[-1]) for num in cmds]

    maze = [line.replace('\n', '') for line in lines[0:-2]]
    m_len = max(len(line) for line in maze)
    maze = [" " * (m_len+2)] + [" " + line + (" " * (m_len - len(line)) + " ") for line in maze] + [" " * (m_len+2)]

    print("0123456789")
    for line in maze:
        print(line)
    quit()


    pos = (maze[0].index('.'), 0)
    print(pos)
    facing = 0 #0 is right, 1 is down, 2 is left, 3 is up
    for num, end_rot in cmds:
        for _ in range(0, num):
            if facing == 0:
                next_pos = (pos[0] + 1, pos[1])
            elif facing == 2:
                next_pos = (pos[0] - 1, pos[1])
            elif facing == 1:
                next_pos = (pos[0], pos[1] + 1)
            elif facing == 3:
                next_pos = (pos[0], pos[1] - 1)
            else:
                raise Exception(f"Facing error {facing}")

            next_pos = calc_wrap(maze, next_pos, facing)
            if check_wall(maze, next_pos):
                break
            pos = next_pos
            print(pos)

        if end_rot == "R":
            facing = (facing+1)%4
        elif end_rot == "L":
            facing = (facing-1)%4


    result = 1000 * (pos[1]+1) + 4 * (pos[0]+1) + facing
    print(result)
