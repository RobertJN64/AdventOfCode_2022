def main():
    with open("Day02/day02.txt") as f:
        lines = f.readlines()

    score = 0
    for line in lines:
        opp, you = line.strip().split(" ")
        if you == "X":
            score += 1
            if opp == "A":
                score += 3
            if opp == "C":
                score += 6

        if you == "Y":
            score += 2
            if opp == "B":
                score += 3
            if opp == "A":
                score += 6

        if you == "Z":
            score += 3
            if opp == "C":
                score += 3
            if opp == "B":
                score += 6

    print(score)

