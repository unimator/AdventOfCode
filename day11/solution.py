class Monkey:
    def __init__(self, items, operation, predicate, if_true_monkey, if_false_monkey):
        self.items = items
        self.operation = operation
        self.predicate = predicate
        self.if_true_monkey = if_true_monkey
        self.if_false_monkey = if_false_monkey
        self.inspections = 0

max_divisor = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
def do_task(worry_divisor, rounds_count):
    monkeys = []
    with open('input', 'r') as input_file:
        groups = input_file.read().split('\n\n')
        for group in groups:
            group = group.split('\n')
            items = eval('[%s]' % group[1].split(':')[1].strip())
            operation = group[2].split('=')[1].strip()
            predicate = int(group[3].split('by')[1].strip())
            if_true_monkey = int(group[4].split('monkey')[1].strip())
            if_false_monkey = int(group[5].split('monkey')[1].strip())
            monkeys.append(Monkey(items, operation, predicate, if_true_monkey, if_false_monkey))
    
    def round(monkey):
        while len(monkey.items) > 0:
            item = monkey.items.pop()
            monkey.inspections += 1
            old = item
            worry_level = eval(monkey.operation)
            worry_level /= worry_divisor
            worry_level = int(worry_level)
            worry_level %= max_divisor
            if worry_level % monkey.predicate == 0:
                monkeys[monkey.if_true_monkey].items.append(worry_level)
            else:
                monkeys[monkey.if_false_monkey].items.append(worry_level)

    for i in range(rounds_count):
        for monkey in monkeys:
            round(monkey)

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse=True)

    return inspections[0] * inspections[1]

# Task A
print(do_task(3, 20))

# Task B
print(do_task(1, 10000))