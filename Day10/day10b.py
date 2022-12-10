def main():
    with open("Day10/day10.txt") as f:
        lines = f.read()

    X = 1
    crt = ['.'] * 240

    lines = lines.replace("addx", "noop\naddx")
    lines = lines.split("\n")
    score = 0
    for cycle, item in enumerate(lines):
        crt_pos = cycle % 40
        if abs(crt_pos - X) < 2:
            crt[cycle] = '#'
        else:
            crt[cycle] = ' '

        #print(item)
        if "addx" in item:
            num = int(item.split(" ")[1])
            X += num

        if (cycle+2) % 40 == 20:
            score += (cycle+2) * X
            print(cycle + 2, X)



    print(score)

    for i in range(0, 240, 40):
        print(''.join(crt[i:i+40]))



