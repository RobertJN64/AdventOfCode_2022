def main():
    with open("Day06/day06.txt") as f:
        line = f.read()

    last14 = " " * 14
    for index, char in enumerate(line):
        last14 = last14[1:]
        last14 += char

        if len(set(last14)) == 14 and " " not in last14:
            print(index+1)
            break
