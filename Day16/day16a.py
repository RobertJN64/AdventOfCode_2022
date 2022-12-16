import copy


class Valve:
    def __init__(self, line):
        line = line.replace(",", "").replace("=", " ").replace(";", "").strip().split(" ")
        self.id = line[1]
        self.flow_rate = int(line[5])
        self.paths = line[10:]

    def __repr__(self):
        return f"Valve {self.id} with flow rate {self.flow_rate} | tunnels: {self.paths}"

class Tunnel:
    def __init__(self, point_a, point_b, length):
        self.point_a = point_a
        self.point_b = point_b
        self.length = length

    def __repr__(self):
        return f"Tunnel of length {self.length} between {self.point_a} and {self.point_b}"

class Q:
    def __init__(self):
        self.location = 'AA'
        self.timer = 0
        self.open_valves = []
        self.total_flow_rate = 0
        self.active_flow_rate = 0
        self.last_loc = ''

        self.location_db = {'AA': 0}
        self.turn_time = []
        self.flow_hist = []

    def update(self):
        self.total_flow_rate += self.active_flow_rate
        self.location_db[self.location] = self.active_flow_rate
        self.flow_hist.append(self.active_flow_rate)


def main():
    with open("Day16/day16.txt") as f:
        lines = f.readlines()

    valve_db = {}
    for line in lines:
        v = Valve(line)
        valve_db[v.id] = v

    # METHOD: 0 point compression
    # Goal: Create optimized datastructure of paths

    #STEP 1: Convert valve_db into tunnel list

    tunnels = []
    for v in valve_db.values():
        for path in v.paths:
            # CHECK FOR DUPS
            for t in tunnels:
                if t.point_a == path and t.point_b == v.id:
                    break
            else:
                tunnels.append(Tunnel(v.id, path, 1))

    #STEP 2: Combine tunnels with 0 flow rate middle and exactly 2 exits

    for v in valve_db.values():
        if v.flow_rate == 0 and len(v.paths) == 2:
            t_comb_list = []
            for t in tunnels:
                if t.point_a == v.id or t.point_b == v.id:
                    t_comb_list.append(t)

            assert len(t_comb_list) == 2
            for item in t_comb_list:
                tunnels.remove(item)
            t_shared_points = set()
            for t in t_comb_list:
                t_shared_points.add(t.point_a)
                t_shared_points.add(t.point_b)
            t_shared_points.remove(v.id)
            t_shared_points = list(t_shared_points)
            tunnels.append(Tunnel(t_shared_points[0], t_shared_points[1], t_comb_list[0].length + t_comb_list[1].length))


    print(tunnels)
    queue = [Q()]

    correct_v = ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']
    correct_t = [1, 4, 8, 16, 20, 23]

    best_flow = 1000
    def add_q(_qt: Q):
        nonlocal best_flow
        if _qt.timer >= 29:
            if qt.total_flow_rate > best_flow:# and str(qt.open_valves) == str(correct_v) and str(qt.turn_time) == str(correct_t):
                print("Found solution with flow rate: ", qt.total_flow_rate, qt.active_flow_rate, qt.open_valves, qt.turn_time, qt.flow_hist)
                best_flow = qt.total_flow_rate
        else:
            queue.append(_qt)

    #STEP 3 - search through tunnels
    counter = 0
    while queue:
        q = queue.pop()
        counter += 1
        if counter%10000 == 0:
            print(q.timer, len(queue))
        q.update()
        if q.location not in q.open_valves and valve_db[q.location].flow_rate != 0:
            qt = copy.deepcopy(q)
            qt.open_valves.append(q.location)
            qt.turn_time.append(qt.timer)
            qt.active_flow_rate += valve_db[q.location].flow_rate
            qt.timer += 1
            qt.last_loc = '' # we can return anywhere now
            add_q(qt)

        for t in tunnels:
            if t.point_a == q.location and t.point_b != q.last_loc:
                qt = copy.deepcopy(q)
                qt.last_loc = q.location
                qt.timer += t.length

                for i in range(t.length - 1):
                    qt.update()
                qt.location = t.point_b

                if qt.location not in qt.location_db:
                    add_q(qt)
                elif qt.location_db[qt.location] != qt.active_flow_rate:
                    add_q(qt)

            if t.point_b == q.location and t.point_a != q.last_loc:
                qt = copy.deepcopy(q)
                qt.last_loc = q.location

                qt.timer += t.length

                for i in range(t.length - 1):
                    qt.update()
                qt.location = t.point_a

                if qt.location not in qt.location_db:
                    add_q(qt)
                elif qt.location_db[qt.location] != qt.active_flow_rate:
                    add_q(qt)

        #OPTION - SKIP TO END
        qt = copy.deepcopy(q)
        r_time = 29 - qt.timer
        qt.timer += r_time
        for _ in range(r_time):
            qt.update()
            #qt.total_flow_rate += qt.active_flow_rate * r_time
        add_q(qt)

        #IMPROPERLY CALC FLOW RATE IN MULTI STEP TUNNELS