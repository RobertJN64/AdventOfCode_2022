def main():
    with open("Day06/day06.txt") as f:
        line = f.read()

    last4 = " " * 4
    for index, char in enumerate(line):
        last4 = last4[1:]
        last4 += char

        if len(set(last4)) == 4 and " " not in last4:
            print(index+1)
            break
