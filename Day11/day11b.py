class MathOpp:
    Add = "+"
    Sub = "-"
    Mul = "*"
    Div = "/"
    Null = ""

class Monkey:
    def __init__(self, starting_items, opp, constant, test, true_target, false_target):
        self.items = starting_items
        self.opp = opp
        self.constant = constant
        self.test = test
        self.true_target = true_target
        self.false_target = false_target

        self.counter = 0
        self.sup_c = 1

    def __repr__(self):
        return f"Monkey with items {self.items}"

    def sc(self, sc):
        self.sup_c = sc

    def turn(self, others):
        for item in self.items:
            self.counter += 1
            c = self.constant
            if c == "old":
                c = item

            if self.opp == MathOpp.Add:
                item += c
            if self.opp == MathOpp.Sub:
                item -= c
            if self.opp == MathOpp.Mul:
                item *= c
            if self.opp == MathOpp.Div:
                item /= c

            item = item%self.sup_c

            # if (item % self.test == 0) != (a_item % self.test == 0):
            #     print("ERROR B")
            #     quit()

            if item % self.test == 0:
                others[self.true_target].items.append(item)
            else:
                others[self.false_target].items.append(item)
        self.items = []


def process_round(monkeys: list[Monkey]):
    for monkey in monkeys:
        monkey.turn(monkeys)

def main():
    with open("Day11/day11.txt") as f:
        lines = f.read()

    monkey_data = lines.split("Monkey")[1:]
    monkeys = []
    for item in monkey_data:
        lines = item.split("\n")

        starting_items = []
        opp = MathOpp.Null
        constant = 0
        test = 0
        true_target = 0
        false_target = 0

        for line in lines:
            line = line.strip()
            if "Starting items:" in line:
                starting_items = list(map(int, line.replace("Starting items: ", "").split(", ")))
            if "Operation:" in line:
                opp, constant = line.replace("Operation: new = old ", "").split(" ")
                if constant != "old":
                    constant = int(constant)
            if "Test: divisible by " in line:
                test = int(line.replace("Test: divisible by ", ""))
            if "If true: throw to monkey " in line:
                true_target = int(line.replace("If true: throw to monkey ", ""))
            if "If false: throw to monkey " in line:
                false_target = int(line.replace("If false: throw to monkey ", ""))

        monkeys.append(Monkey(starting_items, opp, constant, test, true_target, false_target))

    for monkey in monkeys:
        print(monkey)

    super_constant = 1
    for monkey in monkeys:
        super_constant *= monkey.test
    for monkey in monkeys:
        monkey.sc(super_constant)
    print(super_constant)

    for i in range(0, 10000 ):
        process_round(monkeys)
        print()
    for monkey in monkeys:
        print(monkey)
        print(monkey.counter)
#
    counters = sorted([monkey.counter for monkey in monkeys], reverse=True)
    print(counters[0] * counters[1])


