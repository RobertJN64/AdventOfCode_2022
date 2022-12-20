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
    def __init__(self):
        self.ore_r = 1 #Start with one ore robot
        self.ore = 0
        self.clay_r = 0
        self.clay = 0
        self.obsid_r = 0
        self.obsid = 0
        self.geode_r = 0
        self.geode = 0

        self.timer = 0

    def update(self):
        self.timer += 1
        self.ore += self.ore_r
        self.clay += self.clay_r
        self.obsid += self.obsid_r
        self.geode += self.geode_r

    def __repr__(self):
        return str([self.ore, self.clay, self.obsid, self.geode]) + " | " + str([self.ore_r, self.clay_r, self.geode_r, self.obsid_r])


def can_afford(q: Q, bp: BP):
    r = []
    for cost in [bp.ore, bp.clay, bp.obsid, bp.geode]:
        r.append(cost.ore <= q.ore and cost.clay <= q.clay and cost.obsid <= q.obsid)
    return r

def max_geodes(bp: BP):
    q = Q()
    q.update()
    queue = [q]

    m_geodes = 0
    def add_qt(nqt: Q):
        nonlocal m_geodes
        if nqt.timer >= 15:
            #print(nqt)
            if nqt.geode > m_geodes:
                m_geodes = nqt.geode
                print("Found solution:", m_geodes)
        else:
            queue.append(nqt)

    counter = 0
    while queue:
        q = queue.pop()
        if counter%1000 == 0:
            print(len(queue))
        counter += 1
        ca = can_afford(q, bp)

        if ca[0] and ca[1] and ca[2] and ca[3]:
            continue

        if ca[0]:
            qt = copy.deepcopy(q)
            qt.ore_r += 1
            qt.ore -= bp.ore.ore
            qt.clay -= bp.ore.clay
            qt.obsid -= bp.ore.obsid
            add_qt(qt)
        if ca[1]:
            qt = copy.deepcopy(q)
            qt.clay_r += 1
            qt.ore -= bp.clay.ore
            qt.clay -= bp.clay.clay
            qt.obsid -= bp.clay.obsid
            add_qt(qt)
        if ca[2]:
            qt = copy.deepcopy(q)
            qt.obsid_r += 1
            qt.ore -= bp.obsid.ore
            qt.clay -= bp.obsid.clay
            qt.obsid -= bp.obsid.obsid
            add_qt(qt)
        if ca[3]:
            qt = copy.deepcopy(q)
            qt.geode_r += 1
            qt.ore -= bp.geode.ore
            qt.clay -= bp.geode.clay
            qt.obsid -= bp.geode.obsid
            add_qt(qt)
        q.update()
        add_qt(q)

def main():
    with open("Day19/day19.txt") as f:
        lines = f.readlines()
    bps = [BP(line) for line in lines]

    for bp in bps:
        max_geodes(bp)
        quit()

#SMART DECISION MAKING:
# IF YOU CAN BUY GEODE - BUY GEODE
# ONLY BUY ITEMS IF THEY PAY FOR THEMSELVES