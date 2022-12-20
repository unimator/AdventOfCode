import re

stacks_a = [[] for _ in range(9)]
stacks_b = []
N = 4
GROUPS_NUM = 9
with open('input', 'r') as input_file:
    lines = [line for line in input_file]
    line_it = iter(lines)
    while not line.startswith(' 1'):
        line = next(line_it)
        line_splitted = [line[i:i+N] for i in range(0, len(line), N)]
        for val in range(GROUPS_NUM):
            c = line_splitted[val][1]
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                stacks_a[val].append(c)
    for stack in stacks_a:
        stack.reverse()
    stacks_b = [stack[:] for stack in stacks_a]
    next(line_it)
    pattern = "move (\d+) from (\d+) to (\d+)"
    while True:
        line = next(line_it, None)
        if line == None:
            break
        res = re.match(pattern, line)
        [steps_count, take_from, put_on] = [int(res.group(1)), int(res.group(2)), int(res.group(3))]
        for step in range(steps_count):
            source = stacks_a[take_from - 1]
            target = stacks_a[put_on - 1]
            current = source.pop()
            target.append(current)
        
        source = stacks_b[take_from - 1]
        target = stacks_b[put_on - 1]
        [leave, take] = [source[:-steps_count], source[-steps_count:]]
        stacks_b[take_from - 1] = leave
        stacks_b[put_on - 1] = target + take


task_a_result = ''
task_b_result = ''
for stack_a in stacks_a:
    task_a_result += stack_a[-1]

for stack_b in stacks_b:
    task_b_result += stack_b[-1]

# Task A
print(task_a_result)

# Task B
print(task_b_result)
