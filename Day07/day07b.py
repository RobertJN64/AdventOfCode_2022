import pprint

def find_sizes(d_struct):
    def calc_recursive_size(struct):
        local_size = 0
        for item in struct:
            if item == "files":
                local_size += sum(struct[item])
            else:
                local_size += calc_recursive_size(struct[item])

        return local_size

    del_target_size = 30000000 - (70000000 - calc_recursive_size(d_struct))
    print(del_target_size)

    best_option = 70000000
    def calc_rm_size(struct):
        nonlocal best_option
        local_size = 0
        for item in struct:
            if item == "files":
                local_size += sum(struct[item])
            else:
                local_size += calc_rm_size(struct[item])

        if del_target_size < local_size < best_option:
            best_option = local_size
        print(struct, local_size)
        return local_size

    calc_rm_size(d_struct)
    print(best_option)

def main():
    with open("Day07/day07.txt") as f:
        lines = f.readlines()

    d_struct = {}

    d_pos = []

    index = 0
    while index < len(lines):
        line = lines[index]
        line = line.strip()
        if "$" in line:
            line = line.replace("$ ", "")


            results = []
            while True:
                index += 1
                if index == len(lines):
                    break
                t_line = lines[index]
                t_line = t_line.strip()
                if "$" in t_line:
                    break
                results.append(t_line)

            if "cd" in line:
                line = line.replace("cd ", "")
                if line == "..":
                    d_pos.pop()
                else:
                    d_pos.append(line)


            if "ls" in line:
                c_stuct = d_struct
                for item in d_pos:
                    if item not in c_stuct:
                        c_stuct[item] = {"files": []}
                    c_stuct = c_stuct[item]

                for item in results:
                    if "dir" == item[0:3]:
                        pass
                    else:
                        c_stuct["files"].append(int(item.split(" ")[0]))




        else:
            index += 1

    pprint.pprint(d_struct)
    find_sizes(d_struct)

