state_a = []
state_b = []

#input file has been parsed and split in two by hand

with open('input_initial', 'r') as input_file:
    lines = [line for line in input_file]
    for line in lines:
        stack_a = []
        stack_b = []
        for c in line.strip():
            stack_a.append(c)
            stack_b.append(c)
        state_a.append(stack_a)
        state_b.append(stack_b)

with open('input_steps', 'r') as input_file:
    lines = [line for line in input_file]
    for line in lines:
        [steps_count, take_from, put_on] = [int(x) for x in line.split(' ')]
        for step in range(steps_count):
            source = state_a[take_from - 1]
            target = state_a[put_on - 1]
            current = source.pop()
            target.append(current)
        
        source = state_b[take_from - 1]
        target = state_b[put_on - 1]
        [leave, take] = [source[:-steps_count], source[-steps_count:]]
        state_b[take_from - 1] = leave
        state_b[put_on - 1] = target + take

task_a_result = ''
task_b_result = ''
for stack_a in state_a:
    task_a_result += stack_a[-1]

for stack_b in state_b:
    task_b_result += stack_b[-1]

# Task A
print(task_a_result)

# Task B
print(task_b_result)
