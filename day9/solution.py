board_size = 10
board = [[False for _ in range(board_size)] for _ in range(board_size)]

H = [board_size/2, board_size/2]
T = H
tran_vec = [0, 0]

def taxicab_distance(T1, T2):
    return sum([abs(t1 - t2) for (t1, t2) in zip(T1, T2)])

def s(t):
    if t:
        return '#'
    else:
        return ' '

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
            prev_H = [H[0], H[1]]
            H = [sum(x) for x in zip(H, tran_vec)]
            if taxicab_distance(H, T) == 0:
                pass
            elif H[0] == T[0] or H[1] == T[1] and taxicab_distance(H, T) == 2:
                T = [prev_H[0], prev_H[1]]
            elif taxicab_distance(H, T) > 2:
                T = [prev_H[0], prev_H[1]]
            if T[0] < 0 or T[1] < 0:
                raise ValueError('Out of range index')
            board[T[0]][T[1]] = True
            print('S %s' % line)
            for x in range(board_size):
                print([s(z) for z in board[x]])
    task_a_sum = 0
    for x in range(board_size):
        for y in range(board_size):
            if board[x][y] == True:
                task_a_sum += 1

# Task A
print(task_a_sum)
