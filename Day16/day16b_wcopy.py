import copy

END_TIME = 26 * 2 - 2

cutoff_loc_AFR_1 = [{} for _ in range(END_TIME + 2)]
cutoff_loc_AFR_2 = [{} for _ in range(END_TIME + 2)]
cutoff_loc_TFR = [{} for _ in range(END_TIME + 2)]

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
    def __init__(self, location_1='AA', location_2='AA', timer=0, open_valves=None, total_flow_rate=0,
                 active_flow_rate_1=0, active_flow_rate_2=0, location_list_1=None, location_list_2=None,
                 done_1=False, done_2=False):
        self.location_1 = location_1
        self.location_2 = location_2

        self.timer = timer

        if open_valves is None:
            self.open_valves = []
            self.g_open_valves = False
        else:
            self.open_valves = open_valves
            self.g_open_valves = True

        self.active_flow_rate_1 = active_flow_rate_1
        self.active_flow_rate_2 = active_flow_rate_2
        self.total_flow_rate = total_flow_rate

        self.done_1 = done_1
        self.done_2 = done_2

        def loc_list(x):
            if x is None:
                return set(), False
            else:
                return x, True
        self.location_list_1, self.g_location_list_1 = loc_list(location_list_1)
        self.location_list_2, self.g_location_list_2 = loc_list(location_list_2)

    def update_flow_counter(self):
        if self.timer%2 == 0:
            if self.g_location_list_1:
                self.location_list_1 = copy.copy(self.location_list_1)
                self.g_location_list_1 = False
            self.location_list_1.add(self.location_1)

            self.total_flow_rate += self.active_flow_rate_1 + self.active_flow_rate_2

        else:
            if self.g_location_list_2:
                self.location_list_2 = copy.copy(self.location_list_2)
                self.g_location_list_2 = False
            self.location_list_2.add(self.location_2)

        self.timer += 1

        c_loc_1 = self.location_1 + self.location_2
        c_loc_2 = self.location_2 + self.location_1
        cafr_1 = cutoff_loc_AFR_1[self.timer].get(c_loc_1, -1)
        cafr_2 = cutoff_loc_AFR_2[self.timer].get(c_loc_1, -1)
        ctfr = cutoff_loc_TFR[self.timer].get(c_loc_1, -1)
        if self.active_flow_rate_1 > cafr_1 and self.active_flow_rate_2 > cafr_2 and self.total_flow_rate > ctfr:
            cutoff_loc_AFR_1[self.timer][c_loc_1] = self.active_flow_rate_1
            cutoff_loc_AFR_2[self.timer][c_loc_1] = self.active_flow_rate_2
            cutoff_loc_TFR[self.timer][c_loc_1] = self.total_flow_rate
            cutoff_loc_AFR_1[self.timer][c_loc_2] = self.active_flow_rate_1
            cutoff_loc_AFR_2[self.timer][c_loc_2] = self.active_flow_rate_2
            cutoff_loc_TFR[self.timer][c_loc_2] = self.total_flow_rate


        return not (self.active_flow_rate_1 < cafr_1 and self.active_flow_rate_2 < cafr_2 and self.total_flow_rate < ctfr)

    def open_valve(self, valve_db):
        if self.g_open_valves:
            self.open_valves = copy.copy(self.open_valves)
            self.g_open_valves = False

        if self.timer%2 == 1: #INVERT BECAUSE UPDATE FLOW RATE IS CALLED FIRST
            self.open_valves.append(self.location_1)
            self.active_flow_rate_1 += valve_db[self.location_1].flow_rate
            self.location_list_1 = set()
            self.g_location_list_1 = False

        else:
            self.open_valves.append(self.location_2)
            self.active_flow_rate_2 += valve_db[self.location_2].flow_rate
            self.location_list_2 = set()
            self.g_location_list_2 = False


    def fast_copy(self):
        q = Q(self.location_1, self.location_2, self.timer, self.open_valves, self.total_flow_rate,
                 self.active_flow_rate_1, self.active_flow_rate_2, self.location_list_1, self.location_list_2,
                 self.done_1, self.done_2)
        return q

def main():
    with open("day16.txt") as f:
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
    best_flow = -1

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

        if q.timer%2 == 0:
            if q.done_1:
                q.update_flow_counter()
                add_q(q)
                continue
            loc = q.location_1
            loc_list = q.location_list_1
        else:
            loc = q.location_2
            loc_list = q.location_list_2
            if q.done_2 and not q.done_1:
                q.update_flow_counter()
                add_q(q)
                continue


        no_path = True

        if loc not in q.open_valves and valve_db[loc].flow_rate != 0:
            def open_valve():
                nonlocal no_path
                qt = q.fast_copy()
                if qt.update_flow_counter():
                    qt.open_valve(valve_db)
                    add_q(qt)
                    no_path = False

            open_valve()

        for t in tunnel_hash_table[loc]:
            def check_travel(current, target):
                nonlocal no_path
                if current == loc and target not in loc_list:
                    qt = q.fast_copy()
                    if qt.update_flow_counter():
                        if qt.timer%2 == 1:
                            qt.location_1 = target
                        else:
                            qt.location_2 = target
                        add_q(qt)
                        no_path = False

            check_travel(t.point_a, t.point_b)
            check_travel(t.point_b, t.point_a)

        if no_path:
            if q.timer%2 == 0:
                q.done_1 = True
            else:
                q.done_2 = True
            add_q(q)

        if q.done_1 and q.done_2 and q.timer%2 == 1:
            # while q.timer < END_TIME:
            #     q.update_flow_counter()
            q.total_flow_rate += (q.active_flow_rate_1 + q.active_flow_rate_2) * int((END_TIME - q.timer)/2)
            q.timer = END_TIME
            add_q(q)
