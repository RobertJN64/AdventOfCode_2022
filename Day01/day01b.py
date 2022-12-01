def main():
    with open("Day01/day01b.txt") as f:
        lines = f.readlines()

    counts = []
    current_count = 0
    for item in lines:
        item = item.strip()
        if item == "":
            counts.append(current_count)
            current_count = 0
        else:
            item = int(item)
            current_count += item

    counts = sorted(counts, reverse=True)
    print(sum(counts[0:3]))