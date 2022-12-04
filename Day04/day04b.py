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
            if item in list(range(bS, bE + 1)):
                counter += 1
                found = True
                break

        if not found:
            for item in list(range(bS, bE + 1)):
                if item in list(range(aS, aE + 1)):
                    counter += 1
                    break

    print(counter)