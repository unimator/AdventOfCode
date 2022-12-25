GRID_WIDTH = 150
GRID_HEIGHT = 200
grid = [_ for _ in range(GRID_HEIGHT)]

with open('input', 'r') as input_file:
    for i in range(GRID_HEIGHT):
        line = next(input_file)
        line = line[:-1] + ' ' * (GRID_WIDTH - len(line) + 1)
        grid[i] = line

    next(input_file) # skip empty line
    moves = next(input_file)

start_position = (0, 0)
while grid[start_position[0]][start_position[1]] != '.':
    start_position = (start_position[0], start_position[1] + 1)

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def flat_move(position, count, facing, rotation):
    new_position = position
    while count > 0:
        ny, nx = new_position
        dy, dx  = direction[facing]
        (ny, nx) = (ny + dy, nx + dx)
        if nx >= GRID_WIDTH:
            nx = 0
        if nx < 0:
            nx = GRID_WIDTH - 1
        if ny >= GRID_HEIGHT:
            ny = 0
        if ny < 0:
            ny = GRID_HEIGHT - 1
        new_position = (ny, nx)
        if grid[ny][nx] == ' ':
            continue
        if grid[ny][nx] == '#':
            break
        position = new_position
        count -= 1
    facing = (facing + rotation) % len(direction)
    return (position, facing)

def cube_move(position, count, facing, rotation):
    new_position = position
    while count > 0:
        ny, nx = new_position
        dy, dx  = direction[facing]
        (ny, nx) = (ny + dy, nx + dx)
        last_facing = facing

        # B -> F
        if ny < 0 and nx >= 50 and nx < 100:
            ny = 100 + nx
            nx = 0
            facing = 0
        # F -> B
        if ny >= 150 and ny < GRID_HEIGHT and nx < 0:
            nx = ny - 100
            ny = 0
            facing = 1
        # A -> F
        if ny < 0 and nx >= 100:
            ny = GRID_HEIGHT - 1
            nx = nx - 100
            facing = 3
        # F -> A
        if ny >= GRID_HEIGHT and nx < 50:
            ny = 0
            nx = nx + 100
            facing = 1
        # A -> C
        if nx >= 100 and ny >= 50 and facing == 1:
            ny = nx - 50
            nx = 100 - 1
            facing = 2
        # C -> A
        if nx >= 100 and ny >= 50 and ny < 100 and facing == 0:
            nx = ny + 50
            ny = 50 - 1
            facing = 3
        # D -> F
        if nx >= 50 and nx < 100 and ny >= 150 and facing == 1:
            ny = nx + 100
            nx = 50 - 1
            facing = 2
        # F -> D
        if nx >= 50 and ny >= 150 and ny < GRID_HEIGHT and facing == 0:
            nx = ny - 100
            ny = 150 - 1
            facing = 3
        # A -> D
        if nx >= GRID_WIDTH and ny >= 0 and ny < 50:
            nx = 100 - 1
            ny = 150 - ny - 1
            facing = 2
        # D -> A
        if nx >= 100 and ny >= 100 and ny < 150:
            nx = GRID_WIDTH - 1
            ny = 50 - (ny - 100) - 1
            facing = 2
        # C -> E
        if nx < 50 and ny > 50 and ny < 100 and facing == 2:
            nx = ny - 50
            ny = 100
            facing = 1
        # E -> C
        if nx >= 0 and nx < 50 and ny < 100 and facing == 3:
            ny = 50 + nx
            nx = 50
            facing = 0
        # B -> E
        if nx < 50 and ny >= 0 and ny < 50:
            nx = 0
            ny = 150 - ny - 1
            facing = 0
        # E -> B
        if nx < 0 and ny >= 100 and ny < 150:
            nx = 50
            ny = 50 - (ny - 100) - 1
            facing = 0
        
        new_position = (ny, nx)
        if grid[ny][nx] == ' ':
            raise ValueError('Out of all box faces')
        if grid[ny][nx] == '#':
            facing = last_facing
            break
        position = new_position
        count -= 1
    facing = (facing + rotation) % len(direction)
    return (position, facing)

def solve(position, move_method):
    facing = 0
    movement_count = 0
    rotation = None

    for c in moves:
        if c.isdigit():
            movement_count *= 10
            movement_count += int(c)
        else:
            rotation = 1 if c == 'R' else -1
        
        if rotation != None:
            position, facing = move_method(position, movement_count, facing, rotation)
            movement_count = 0
            rotation = None

    position, facing = move_method(position, movement_count, facing, 0)
    return (position, facing)

position, facing = solve(start_position, flat_move)
y, x = position

# Task A
print(1000 * (y + 1) + 4 * (x + 1) + facing)


position, facing = solve(start_position, cube_move)
y, x = position

# Task B
print(1000 * (y + 1) + 4 * (x + 1) + facing)