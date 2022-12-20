import copy

class Cost:
    def __init__(self, ore, clay, obsid):
        self.ore = ore
        self.clay = clay
        self.obsid = obsid

def handle_line(item):
    _, item = item.split("costs ")
    items = item.split(" and ")
    ore = 0
    clay = 0
    obsid = 0
    for item in items:
        count, name = item.split(" ")
        if name == "ore":
            ore = int(count)
        if name == "clay":
            clay = int(count)
        if name == "obsidian":
            obsid = int(count)
    return Cost(ore, clay, obsid)

class BP:
    def __init__(self, line: str):
        _, line = line.split(": ")
        items = line.split(".")[:-1]
        self.ore = handle_line(items[0].strip())
        self.clay = handle_line(items[1].strip())
        self.obsid = handle_line(items[2].strip())
        self.geode = handle_line(items[3].strip())

class Q:
    def __init__(self, goal):
        self.ore_r = 1 #Start with one ore robot
        self.ore = 0
        self.clay_r = 0
        self.clay = 0
        self.obsid_r = 0
        self.obsid = 0
        self.geode_r = 0
        self.geode = 0

        self.timer = 0
        self.goal = goal

    def update(self):
        self.timer += 1
        self.ore += self.ore_r
        self.clay += self.clay_r
        self.obsid += self.obsid_r
        self.geode += self.geode_r

    def __repr__(self):
        return str([self.ore, self.clay, self.obsid, self.geode]) + " | " + str([self.ore_r, self.clay_r, self.obsid_r, self.geode_r])


def can_afford(q: Q, bp: BP):
    cost = [bp.ore, bp.clay, bp.obsid, bp.geode][q.goal]
    return cost.ore <= q.ore and cost.clay <= q.clay and cost.obsid <= q.obsid


def max_geodes(bp: BP):
    queue = [Q(i) for i in range(0, 4)]

    m_geodes = 0
    def add_qt(nqt: Q):
        nonlocal m_geodes
        #print(nqt.timer)
        if nqt.timer >= 22:
            #print(nqt)
            if nqt.geode > m_geodes:
                m_geodes = nqt.geode
                print(nqt)
                print("Found solution:", m_geodes)
        else:
            queue.append(nqt)

    def add_all_qt(nqt: Q):
        for i in range(0, 4):
            qt = copy.deepcopy(nqt)
            qt.goal = i
            add_qt(qt)

    while queue:
        q = queue.pop()
        q.update()
        #print(len(queue))
        if can_afford(q, bp):
            if q.goal == 0:
                q.ore_r += 1
                cost = bp.ore
            elif q.goal == 1:
                q.clay_r += 1
                cost = bp.clay
            elif q.goal == 2:
                q.obsid_r += 1
                cost = bp.obsid
            elif q.goal == 3:
                q.geode_r += 1
                cost = bp.geode
            else:
                raise UserWarning(f"Invalid goal {q.goal}")

            q.ore -= cost.ore
            q.clay -= cost.clay
            q.obsid -= cost.obsid
            add_all_qt(q)
        else:
            add_qt(q)

def main():
    with open("Day19/day19.txt") as f:
        lines = f.readlines()
    bps = [BP(line) for line in lines]

    for bp in bps:
        max_geodes(bp)
        quit()