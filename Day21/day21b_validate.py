import copy

def main():
    with open("Day21/day21.txt") as f:
        lines = f.readlines()

    counters = {}
    for line in lines:
        for symbol in ":+*-/":
            line = line.strip().replace(symbol, "")
        line = line.split(" ")
        for word in line:
            if word != "" and word[0].isalpha():
                if word in counters:
                    counters[word] += 1
                else:
                    counters[word] = 1

    for key, value in counters.items():
        if value != 2:
            print(key, value)
