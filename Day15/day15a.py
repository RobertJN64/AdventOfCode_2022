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
    max_d = max((sb.dist for sb in sb_data))
    min_x = min((sb.s_x for sb in sb_data))
    max_x = max((sb.s_x for sb in sb_data))
    print(max_d, min_x, max_x)

    blocked_counter = 0
    y_row = 2000000
    for xpos in range(min_x - max_d - 10, max_x + max_d + 10):
        if xpos%10000 == 0:
            print(xpos, max_x + max_d + 10)
        for sb in sb_data:
            if sb.b_x == xpos and sb.b_y == y_row:
                #print(xpos, y_row, "blocked by beacon.", blocked_counter)
                #blocked_counter += 1
                break
            if dist(sb.s_x, sb.s_y, xpos, y_row) <= sb.dist:
                #print(xpos, y_row, "blocked by sensor.", blocked_counter)
                blocked_counter += 1
                break

    print(blocked_counter)

    #GOAL - for each point on row - find distance to each sensor. If sensor any sensor did not find closer beacon - empty
    #Else - possible