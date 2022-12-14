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
    def __init__(self, goal, ore_r = 1, ore = 0, clay_r = 0, clay = 0, obsid_r = 0, obsid = 0, geode_r = 0, geode = 0,
                 timer = 0):
        self.ore_r = ore_r #Start with one ore robot
        self.ore = ore
        self.clay_r = clay_r
        self.clay = clay
        self.obsid_r = obsid_r
        self.obsid = obsid
        self.geode_r = geode_r
        self.geode = geode

        self.timer = timer
        self.goal = goal

    def update(self):
        self.timer += 1
        self.ore += self.ore_r
        self.clay += self.clay_r
        self.obsid += self.obsid_r
        self.geode += self.geode_r

    def __repr__(self):
        return str(self.timer) + " _ " + str(self.goal) + ": " + str([self.ore, self.clay, self.obsid, self.geode]) + " | " + str([self.ore_r, self.clay_r, self.obsid_r, self.geode_r])


def can_afford(q: Q, bp: BP):
    cost = [bp.ore, bp.clay, bp.obsid, bp.geode][q.goal]
    return cost.ore <= q.ore and cost.clay <= q.clay and cost.obsid <= q.obsid


def max_geodes(bp: BP):
    queue = [Q(i) for i in range(0, 4)]


    m_geodes = 0
    def add_qt(nqt: Q):
        nonlocal m_geodes
        if nqt.timer >= 24:
            if nqt.geode > m_geodes:
                m_geodes = nqt.geode
                print(nqt)
                print("Found solution:", m_geodes)
        else:
            queue.append(nqt)

    def add_all_qt(nqt: Q):
        for i in range(0, 4):
            qt = Q(nqt.goal, nqt.ore_r, nqt.ore, nqt.clay_r, nqt.clay, nqt.obsid_r, nqt.obsid, nqt.geode_r, nqt.geode,
                   nqt.timer)
            qt.update()
            qt.goal = i
            add_qt(qt)

    #counter = 0
    while queue:
        # if counter%10000 == 0:
        #     print(counter, queue[0].timer, len(queue))
        # counter += 1
        q = queue.pop()
        #print(len(queue))
        if can_afford(q, bp):
            if q.goal == 0:
                q.ore_r += 1
                q.ore -= 1 #cancels out new purchase
                cost = bp.ore
            elif q.goal == 1:
                q.clay_r += 1
                q.clay -= 1
                cost = bp.clay
            elif q.goal == 2:
                q.obsid_r += 1
                q.obsid -= 1
                cost = bp.obsid
            elif q.goal == 3:
                q.geode_r += 1
                q.geode -= 1
                cost = bp.geode
            else:
                raise UserWarning(f"Invalid goal {q.goal}")

            q.ore -= cost.ore
            q.clay -= cost.clay
            q.obsid -= cost.obsid
            add_all_qt(q)

        else:
            q.update()
            add_qt(q)

    return m_geodes

def main():
    with open("Day19/day19.txt") as f:
        lines = f.readlines()
    bps = [BP(line) for line in lines]

    for bp in bps:
        print("NEW BP")
        m = max_geodes(bp)
        print(m)