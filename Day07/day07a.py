import pprint

def find_sizes(d_struct):
    under_1k_size_counter = 0

    def calc_recursive_size(struct):
        nonlocal under_1k_size_counter
        local_size = 0
        for item in struct:
            if item == "files":
                local_size += sum(struct[item])
            else:
                local_size += calc_recursive_size(struct[item])
        if local_size < 100000:
            under_1k_size_counter += local_size

        print("Local Size of", struct, "was", local_size)
        return local_size

    calc_recursive_size(d_struct)
    print(under_1k_size_counter)


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
            print("Processing cmd: ", line)

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
                    print(d_pos)

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

