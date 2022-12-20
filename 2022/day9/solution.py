from __future__ import print_function

board_size = 1000
board_a = [[False for _ in range(board_size)] for _ in range(board_size)]
board_b = [[False for _ in range(board_size)] for _ in range(board_size)]

H = [0, 0]
T = H
knots_count = 9
knots = [T[:] for _ in range(knots_count)]
tran_vec = [0, 0]

def taxicab_distance(T1, T2):
    return sum([abs(t1 - t2) for (t1, t2) in zip(T1, T2)])

def find_closest_diagonal(next_knot, current_knot):
    for T in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
        new_knot = [sum(t) for t in zip(next_knot, T)]
        if taxicab_distance(new_knot, current_knot) <= 2:
            return T

def find_closest_inline(next_knot, current_knot):
    for T in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            new_knot = [sum(t) for t in zip(next_knot, T)]
            if taxicab_distance(new_knot, current_knot) == 1:
                return T

def try_update_knot(knot, index):
    if index == knots_count:
        return
    knot_current = knots[index]
    if (knot[0] == knot_current[0] or knot[1] == knot_current[1]) and taxicab_distance(knot, knot_current) > 1:
        best_t = find_closest_inline(knot_current, knot)
        knots[index] = [sum(t) for t in zip(knot_current, best_t)]
    elif taxicab_distance(knot, knot_current) > 2:
        best_t = find_closest_diagonal(knot_current, knot)
        knots[index] = [sum(t) for t in zip(knot_current, best_t)]
    try_update_knot(knots[index], index + 1)

with open('input', 'r') as input_file:
    for line in input_file:
        [direction, steps_str] = line.split(" ")
        steps = int(steps_str)
        direction = direction.strip()

        if direction == 'L':
            tran_vec = [0, -1]
        elif direction == 'R':
            tran_vec = [0, 1]
        elif direction == 'U':
            tran_vec = [1, 0]
        elif direction == 'D':
            tran_vec = [-1, 0]
        else:
            raise ValueError('Out of range %s' % direction)

        for step in range(steps):
            H = [sum(x) for x in zip(H, tran_vec)]
            try_update_knot(H, 0)
            board_a[knots[0][0]][knots[0][1]] = True
            board_b[knots[-1][0]][knots[-1][1]] = True
    task_a_sum = 0
    task_b_sum = 0
    for x in range(board_size):
        for y in range(board_size):
            if board_a[x][y] == True:
                task_a_sum += 1
            if board_b[x][y] == True:
                task_b_sum += 1


# Task A
print(task_a_sum)

# Task B
print(task_b_sum)