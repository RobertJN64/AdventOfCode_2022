def check_wall(maze, pos):
    return maze[pos[1]][pos[0]] == '#'

def calc_wrap(maze, pos, facing):
    x, y = pos
    if y < 0 or (facing == 3 and maze[y][x] == ' '):
        y = len(maze) - 1
        while maze[y][x] == ' ':
            y -= 1
    if y >= len(maze) or (facing == 1 and maze[y][x] == ' '):
        y = 0
        while maze[y][x] == ' ':
            y += 1


    if x < 0 or (facing == 2 and maze[y][x] == ' '):
        x = len(maze[0]) - 1
        while maze[y][x] == ' ':
            x -= 1
    if x >= len(maze[0]) or (facing == 0 and maze[y][x] == ' '):
        x = 0
        while maze[y][x] == ' ':
            x += 1

    return x, y



def main():
    with open("Day22/day22.txt") as f:
        lines = f.readlines()

    cmd_str = lines[-1].strip().replace("L", "L ").replace("R", "R ") + "X" #X is null cmd
    cmds = cmd_str.split(" ")
    cmds = [(int(num[:-1]), num[-1]) for num in cmds]

    maze = [line.replace('\n', '') for line in lines[0:-2]]
    m_len = max(len(line) for line in maze)
    maze = [line + (" " * (m_len - len(line))) for line in maze]

    print("0123456789")
    for line in maze:
        print(line)


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
