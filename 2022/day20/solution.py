with open('input', 'r') as input_file:
    numbers = []
    for i, line in enumerate(input_file):
        numbers.append((i, int(line.strip())))
    
    def mix_numbers(numbers):
        list_size = len(numbers)
        for i in range(list_size):
            num = next(y for (x, y) in numbers if x == i)
            cur_index = numbers.index((i, num))
            new_index = (cur_index + num) % (list_size - 1)
            numbers.remove((i, num))
            if new_index == 0:
                new_index = list_size
            numbers.insert(new_index, (i, num))
    
    task_a_numbers = numbers[:]
    mix_numbers(task_a_numbers)

    task_a_zero_index = 0
    for x, y in task_a_numbers:
        if y == 0:
            break
        task_a_zero_index += 1

    # Task A
    print(sum([task_a_numbers[(task_a_zero_index + i * 1000) % len(task_a_numbers)][1] for i in range(1,4)]))

    decryption_key = 811589153
    task_b_numbers = [(x, y * decryption_key) for x, y in numbers]
    for i in range(10):
        mix_numbers(task_b_numbers)
    
    task_b_zero_index = 0
    for x, y in task_b_numbers:
        if y == 0:
            break
        task_b_zero_index += 1

    # Task B
    print(sum([task_b_numbers[(task_b_zero_index + i * 1000) % len(task_b_numbers)][1] for i in range(1,4)]))