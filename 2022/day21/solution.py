task_a_monkeys_known = {}
task_a_monkeys_unknown = {}

task_b_monkeys_known = {}
task_b_monkeys_unknown = {}

def isnumber(str):
    try:
        int(str)
    except ValueError:
        return False
    else:
        return True

root_monkey = None

with open('input', 'r') as input_file:
    for line in input_file:
        [monkey, operation] = line.split(':')
        operation = operation.strip()
        if isnumber(operation):
            task_a_monkeys_known[monkey] = int(operation)
            task_b_monkeys_known[monkey] = int(operation)
        else:
            [left, op, right] = operation.split(' ')
            task_a_monkeys_unknown[monkey] = (left, op, right)
            task_b_monkeys_unknown[monkey] = (left, op, right)

task_b_monkeys_known['humn'] = 'X'
(root_l, root_op, root_r) = task_b_monkeys_unknown['root']
task_b_monkeys_unknown['root'] = (root_l, '=', root_r)

def evaluate(left, right, op):
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        return left / right
    raise ValueError('Unknown op')

while len(task_a_monkeys_unknown) > 0:
    for monkey_unknown in task_a_monkeys_unknown:
        (left, op, right) = task_a_monkeys_unknown[monkey_unknown]
        if left not in task_a_monkeys_known or right not in task_a_monkeys_known:
            continue
        else:
            task_a_monkeys_known[monkey_unknown] = evaluate(task_a_monkeys_known[left], task_a_monkeys_known[right], op)
    for monkey_known in task_a_monkeys_known:
        if monkey_known in task_a_monkeys_unknown:
            del task_a_monkeys_unknown[monkey_known]

# Task A
print(task_a_monkeys_known['root'])

def evaluate_b(left, right, op):
    if not isnumber(left) or not isnumber(right):
        return '(%s %s %s)' % (str(left), str(op), str(right))
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        return left / right
    raise ValueError('Unknown op')

while len(task_b_monkeys_unknown) > 0:
    for monkey_unknown in task_b_monkeys_unknown:
        (left, op, right) = task_b_monkeys_unknown[monkey_unknown]
        if left not in task_b_monkeys_known or right not in task_b_monkeys_known:
            continue
        else:
            left = task_b_monkeys_known[left] if left in task_b_monkeys_known else left
            right = task_b_monkeys_known[right] if right in task_b_monkeys_known else right
            if not isnumber(right):
                tmp = left
                left = right
                right = tmp
            task_b_monkeys_known[monkey_unknown] = evaluate_b(left, right, op)
    for monkey_known in task_b_monkeys_known:
        if monkey_known in task_b_monkeys_unknown:
            del task_b_monkeys_unknown[monkey_known]

print(task_b_monkeys_known['root'])

# (Y - 116154256834924) * 2 = 118841721834931

lX = -1000000000000000
rX = 1000000000000000
while True:
    expr = '(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((X + 816) + 497) / 3) - 395) * 45) + 560) * 2) - 671) + 794) + 697) / 5) + 558) * 4) - 284) / 10) - 428) / 3) + 438) * 32) + 984) / 8) - 802) * 10) + 694) / 2) - 486) * 2) + 97) * 2) - 161) + 958) / 3) - 384) * 2) + 928) / 2) + 633) / 2) - 773) * 2) - 19) * 2) + 904) / 10) - 59) * 8) + 337) + 389) / 6) - 146) * 3) + 446) + 918) / 5) - 606) * 11) + 228) + 746) + 477) / 5) - 638) / 5) + 628) * 2) - 792) / 2) + 298) * 22) + 146) / 2) - 118841721834931) * 2))'
    # expr_lX = expr.replace('X', lX)
    # expr_rX = expr.replace('X', rX)
    # expr_l = eval(expr_lX)
    # expr_r = eval(expr_rX)
    # l_dist = abs(expr_l)
    # r_dist = abs(expr_r)
    # if r_dist > l_dist:
    #     rX = 