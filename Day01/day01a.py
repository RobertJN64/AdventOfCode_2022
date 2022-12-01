def main():
    with open("Day01/day01a.txt") as f:
        lines = f.readlines()

    max_count = 0
    current_count = 0
    for item in lines:
        item = item.strip()
        if item == "":
            if current_count > max_count:
                max_count = current_count
            current_count = 0
        else:
            item = int(item)
            current_count += item

    print(max_count)
