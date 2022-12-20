X = 1
CRT = 1
cycle_count = 0
cycles = [20, 60, 100, 140, 180, 220]
task_a_result = 0
screen_width = 40
screen_height = 6

screen = [['.' for _ in range(screen_width)] for _ in range(screen_height)]

def update_cycle():
    global cycle_count, task_a_result, X
    if cycle_count in cycles:
        task_a_result += X * cycle_count
    symbol = ' '
    if abs((cycle_count % screen_width) - X) < 2:
        symbol = '#'
    screen[(cycle_count / screen_width) % screen_height][cycle_count % screen_width] = symbol
    cycle_count += 1

with open('input', 'r') as input_file:
    for line in input_file:
        line = line.strip()
        if 'noop' in line:
            update_cycle()
        else:
            [_, val_str] = line.split(' ')
            val = int(val_str)
            update_cycle()
            update_cycle()
            X += val

    # Task A
    print(task_a_result)


    # Task B (have to rewrite by hand)
    for x in range(screen_height):
        buf = []
        print(''.join(screen[x]))