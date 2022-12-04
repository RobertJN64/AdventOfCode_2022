def main():
    with open("Day04/day04.txt") as f:
        lines = f.readlines()

    counter = 0
    for line in lines:
        a, b = line.strip().split(",")
        aS, aE = map(int, a.split("-"))
        bS, bE = map(int, b.split("-"))

        found = False
        for item in list(range(aS, aE + 1)):
            if item not in list(range(bS, bE + 1)):
                break
        else:
            counter += 1
            found = True

        if not found:
            for item in list(range(bS, bE + 1)):
                if item not in list(range(aS, aE + 1)):
                    break
            else:
                counter += 1

    print(counter)