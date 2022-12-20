cave_size_x = 1000
cave_size_y = 1000
cave = [['.' for _ in range(cave_size_x)] for _ in range(cave_size_y)]

S = [0, 500]
max_y = 0

def create_rock_formation(line):
    prev_point = None
    global max_y
    for point in line.split('->'):
        [x_str, y_str] = point.strip().split(',')
        [x, y] = [int(x_str), int(y_str)]
        if y > max_y:
            max_y = y
        if prev_point == None:
            prev_point = [x, y]
            continue
        [prev_x, prev_y] = prev_point
        [dx, dy] = [x - prev_x, y - prev_y]
        assert(dx * dy == 0)

        if dx != 0:
            sign_x = abs(dx) / dx
            for ix in range(abs(dx) + 1):
                cave[prev_y][prev_x + sign_x * ix] = '#'

        if dy != 0:
            sign_y = abs(dy) / dy
            for iy in range(abs(dy) + 1):
                cave[prev_y + sign_y * iy][prev_x] = '#'

        prev_point = [x, y]

def simulate_sand_unit():
    sand_position = S
    while True:
        if sand_position[0] + 1 >= cave_size_y:
            return False
        if cave[sand_position[0] + 1][sand_position[1]] == '.':
            sand_position = [sand_position[0] + 1, sand_position[1]]
        elif cave[sand_position[0] + 1][sand_position[1] - 1] == '.':
            sand_position = [sand_position[0] + 1, sand_position[1] - 1]
        elif cave[sand_position[0] + 1][sand_position[1] + 1] == '.':
            sand_position = [sand_position[0] + 1, sand_position[1] + 1]
        else:
            cave[sand_position[0]][sand_position[1]] = 'O'
            return True


with open('input', 'r') as input_file:
    for line in input_file:
        create_rock_formation(line)

    sand_units_rested = 0
    while simulate_sand_unit():
        sand_units_rested += 1
    
    # Task A
    print(sand_units_rested)
    
max_y += 2 + 1
cave_size_y = max_y
cave = [['.' for _ in range(cave_size_x)] for _ in range(cave_size_y)]
for i in range(cave_size_x):
    cave[cave_size_y - 1][i] = '#'

cave_size = max_y
with open('input', 'r') as input_file:
    for line in input_file:
        create_rock_formation(line)

    sand_units_rested = 0
    while cave[0][500] != 'O':
        simulate_sand_unit()
        sand_units_rested += 1

    # Task B
    print(sand_units_rested)