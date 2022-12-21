task_a_monkeys_known = {}
task_a_monkeys_unknown = {}

task_b_monkeys_known = {}
task_b_monkeys_unknown = {}

def isnumber(str):
    try:
        float(str)
    except ValueError:
        return False
    else:
        return True

root_monkey = None

with open('2022/day21/input', 'r') as input_file:
    for line in input_file:
        [monkey, operation] = line.split(':')
        operation = operation.strip()
        if isnumber(operation):
            task_a_monkeys_known[monkey] = float(operation)
            task_b_monkeys_known[monkey] = float(operation)
        else:
            [left, op, right] = operation.split(' ')
            task_a_monkeys_unknown[monkey] = (left, op, right)
            task_b_monkeys_unknown[monkey] = (left, op, right)

task_b_monkeys_known['humn'] = 'X' # 3678125418015
(root_l, root_op, root_r) = task_b_monkeys_unknown['root'] # for my nput root_l is an expression and root_r is some calculated value
del task_b_monkeys_unknown['root']

def evaluate_a(left, right, op):
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
            task_a_monkeys_known[monkey_unknown] = evaluate_a(task_a_monkeys_known[left], task_a_monkeys_known[right], op)
    for monkey_known in task_a_monkeys_known:
        if monkey_known in task_a_monkeys_unknown:
            del task_a_monkeys_unknown[monkey_known]

# Task A
print(int(task_a_monkeys_known['root']))

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
            task_b_monkeys_known[monkey_unknown] = evaluate_b(left, right, op)
    for monkey_known in task_b_monkeys_known:
        if monkey_known in task_b_monkeys_unknown:
            del task_b_monkeys_unknown[monkey_known]

expr = task_b_monkeys_known[root_l] + '-' + str(task_b_monkeys_known[root_r])


# Rough approximation
task_b_result = None
best_expr_val = None
min_X = -1000000000000000
max_X = 1000000000000000
while True:
    expr_min_X = expr.replace('X', str(min_X))
    expr_max_X = expr.replace('X', str(max_X))
    min_X_value = eval(expr_min_X)
    max_X_value = eval(expr_max_X)
    min_dist = abs(min_X_value)
    max_dist = abs(max_X_value)
    if abs(min_X_value) < 1:
        task_b_result = int(min_X)
        best_expr_val = min_X_value
        break
    elif abs(max_X_value) < 1:
        task_b_result = int(max_X)
        best_expr_val = max_X_value
        break
    if min_dist < max_dist:
        max_X = (min_X + max_X) / 2
    else:
        min_X = (min_X + max_X) / 2

# Tunning

best_i = 0
for i in range(-10000, 10000):
    expr_val = eval(expr.replace('X', str(task_b_result + i)))
    if abs(expr_val) < abs(best_expr_val):
        best_expr_val = expr_val
        best_i = i

# Task B
print(task_b_result + best_i)