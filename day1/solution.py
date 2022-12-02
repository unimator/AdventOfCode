reindeers = []
current_reinder = 0
max_value = 0
with open('input', 'r') as input_file:
    lines = [line for line in input_file]
    for line in lines:
        try:
            current_reinder += int(line)
        except ValueError:
            reindeers.append(current_reinder)
            if current_reinder > max_value:
                max_value = current_reinder
            current_reinder = 0
            
    reindeers.append(current_reinder)
    if current_reinder > max_value:
        max_value = current_reinder
    # Task A
    print(max_value)
    reindeers.sort()
    reindeers.reverse()
    # Task B
    print(reindeers[0] + reindeers[1] + reindeers[2])