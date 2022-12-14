import copy

END_TIME = 30

cutoff_loc_AFR = [{} for _ in range(31)]
cutoff_loc_TFR = [{} for _ in range(31)]

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
    def __init__(self, location='AA', timer=0, open_valves=None, total_flow_rate=0,
                 active_flow_rate=0, location_list=None):
        self.location = location
        self.timer = timer

        if open_valves is None:
            self.open_valves = []
            self.g_open_valves = False
        else:
            self.open_valves = open_valves
            self.g_open_valves = True

        self.active_flow_rate = active_flow_rate
        self.total_flow_rate = total_flow_rate

        if location_list is None:
            self.location_list = set()
            self.g_location_list = False
        else:
            self.location_list = location_list
            self.g_location_list = True

    def update_flow_counter(self, skipahead = 1):
        self.total_flow_rate += self.active_flow_rate * skipahead
        if self.g_location_list:
            self.location_list = copy.copy(self.location_list)
            self.g_location_list = False
        self.location_list.add(self.location)
        self.timer += skipahead

        cafr = cutoff_loc_AFR[self.timer].get(self.location, -1)
        ctfr = cutoff_loc_TFR[self.timer].get(self.location, -1)
        if self.active_flow_rate > cafr and self.total_flow_rate > ctfr:
            cutoff_loc_AFR[self.timer][self.location] = self.active_flow_rate
            cutoff_loc_TFR[self.timer][self.location] = self.total_flow_rate

        return not (self.active_flow_rate < cafr and self.total_flow_rate < ctfr)

    def open_valve(self, valve_db):
        if self.g_open_valves:
            self.open_valves = copy.copy(self.open_valves)
            self.g_open_valves = False
        self.open_valves.append(self.location)
        self.active_flow_rate += valve_db[self.location].flow_rate

        self.location_list = set()
        self.g_location_list = False


def main():
    with open("Day16/day16.txt") as f:
        lines = f.readlines()

    valve_db = {}
    for line in lines:
        v = Valve(line)
        valve_db[v.id] = v

    # STEP 1: Convert valve_db into tunnel list
    tunnels = []
    for v in valve_db.values():
        for path in v.paths:
            # CHECK FOR DUPS
            for t in tunnels:
                if t.point_a == path and t.point_b == v.id:
                    break
            else:
                tunnels.append(Tunnel(v.id, path, 1))

    # STEP 2: Combine tunnels with 0 flow rate middle and exactly 2 exits
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
            tunnels.append(
                Tunnel(t_shared_points[0], t_shared_points[1], t_comb_list[0].length + t_comb_list[1].length))

    print(len(tunnels), tunnels)

    tunnel_hash_table = {}
    for t in tunnels:
        l = tunnel_hash_table.get(t.point_a, [])
        l.append(t)
        tunnel_hash_table[t.point_a] = l
        l = tunnel_hash_table.get(t.point_b, [])
        l.append(t)
        tunnel_hash_table[t.point_b] = l
    print(tunnel_hash_table)


    queue = [Q()]
    best_flow = 0

    def add_q(qt: Q):
        nonlocal best_flow
        if qt.timer >= END_TIME:
            if qt.total_flow_rate > best_flow:  # and str(qt.open_valves) == str(correct_v) and str(qt.turn_time) == str(correct_t):
                print("Found solution with flow rate: ", qt.total_flow_rate)
                best_flow = qt.total_flow_rate
        else:
            queue.append(qt)

    counter = 0
    while queue:
        q = queue.pop()
        counter += 1
        if counter % 100000 == 0:
            print(len(queue), queue[0].timer)

        if q.location not in q.open_valves and valve_db[q.location].flow_rate != 0:
            def open_valve():
                qt = Q(q.location, q.timer, q.open_valves, q.total_flow_rate, q.active_flow_rate, q.location_list)
                if qt.update_flow_counter():
                    qt.open_valve(valve_db)
                    add_q(qt)

            open_valve()

        for t in tunnel_hash_table[q.location]:
            def check_travel(current, target):
                if current == q.location and target not in q.location_list:
                    if q.timer + t.length > END_TIME:
                        return
                    qt = Q(q.location, q.timer, q.open_valves, q.total_flow_rate, q.active_flow_rate, q.location_list)
                    if qt.update_flow_counter(t.length):
                        qt.location = target
                        add_q(qt)

            check_travel(t.point_a, t.point_b)
            check_travel(t.point_b, t.point_a)

        # OPTION - SKIP TO END
        q.total_flow_rate += q.active_flow_rate * (END_TIME - q.timer)
        q.timer = END_TIME
        add_q(q)
