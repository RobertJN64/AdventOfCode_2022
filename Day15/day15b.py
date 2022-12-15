def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

class SB:
    def __init__(self, line: str):
        s, b = line.replace(",", "").split(":")
        for item in s.split(" "):
            if "x=" in item:
                self.s_x = int(item.replace("x=", ""))
            if "y=" in item:
                self.s_y = int(item.replace("y=", ""))

        for item in b.split(" "):
            if "x=" in item:
                self.b_x = int(item.replace("x=", ""))
            if "y=" in item:
                self.b_y = int(item.replace("y=", ""))

        self.dist = dist(self.b_x, self.b_y, self.s_x, self.s_y)

    def __repr__(self):
        return f"Sensor {self.s_x, self.s_y} beacon {self.b_x, self.b_y} pair. Distance: {self.dist}"

def main():
    with open("Day15/day15.txt") as f:
        lines = f.readlines()
    sb_data = []
    for line in lines:
        sb_data.append(SB(line))

    print(sb_data)

    #METHODOLOGY - XCOORD SKIPAHEAD

    #find close beacon
    #skip to edge for given x coord
    #repeat

    max_x_y = 4000000

    for ypos in range(0, max_x_y):
        if ypos%40000 == 0:
            print(ypos/40000)
        xpos = 0
        while xpos < max_x_y:
            for sb in sb_data:
                if sb.b_x == xpos and sb.b_y == ypos:
                    break

                if dist(sb.s_x, sb.s_y, xpos, ypos) <= sb.dist:
                    #ACTIVATE SKIP AHEAD
                    max_d = sb.dist - abs(sb.s_y - ypos)
                    end_x = sb.s_x + max_d
                    if end_x != xpos:
                        #print("SKIP FROM", ypos, xpos, end_x-1)
                        xpos = end_x - 1 #because inc

                    break
            else:
                print("COORD", xpos, ypos, xpos*4000000+ypos)
            xpos += 1

