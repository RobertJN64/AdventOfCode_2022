import copy

skip = "humn"
root_pair = ["rpjn", "ghjl"]
#root_pair = ["pppw", "sjmn"]

opp = {
    "+": "-",
    "*": "/",
    "-": "+",
    "/": "*"
}

close_opp = {
    "+": "-",
    "*": "/",
    "-": "-",
    "/": "/"
}

value_db = {}

def main():
    with open("Day21/day21.txt") as f:
        lines = [line.strip().replace(":", " =") for line in f.readlines()]

    r = copy.copy(lines)
    done = False
    while not done:
        done = True
        l = copy.copy(r)
        r = []
        print(len(l))
        for line in l:
            if skip in line and skip not in line[0:5]:
                r.append(line)
            if skip not in line and "root" not in line:
                try:
                    constants = line.split(" ")
                    if len(constants) == 5:
                        a = value_db[constants[2]]
                        b = value_db[constants[4]]
                        value_db[constants[0]] = eval(str(a) + constants[3] + str(b))
                    else:
                        value_db[constants[0]] = int(constants[2])
                    done = False
                except:
                    r.append(line)
            if root_pair[0] in value_db:
                tval = value_db[root_pair[0]]
                goal = root_pair[1]

            if root_pair[1] in value_db:
                tval = value_db[root_pair[1]]
                goal = root_pair[0]

    print(value_db)
    value_db[goal] = tval

    print("Goal:", goal)
    tval = eval("tval")
    print("Tval:", tval)
    print("Lines:", r)

    exec(goal + " = " + str(tval))

    next_solve = goal
    while r:
        print(len(r), next_solve)
        for line in r:
            if next_solve in line:
                constants = line.split(" ")
                if constants[2] in value_db:
                    a = value_db[constants[0]]
                    b = value_db[constants[2]]
                    if close_opp[constants[3]] == constants[3]:
                        value_db[constants[4]] = eval(str(b) + close_opp[constants[3]] + str(a))
                    else:
                        value_db[constants[4]] = eval(str(a) + close_opp[constants[3]] + str(b))
                    r.remove(line)
                    next_solve = constants[4]
                    break
                else:
                    a = value_db[constants[0]]
                    c = value_db[constants[4]]
                    value_db[constants[2]] = eval(str(a) + opp[constants[3]] + str(c))
                    r.remove(line)
                    next_solve = constants[2]
                    break

    print(value_db[skip])