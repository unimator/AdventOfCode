grid = []

with open('input', 'r') as input_file:
    for line in input_file:
        row = []
        line = line.strip()
        for tree in line:
            tree_num = int(tree)
            row.append(tree_num)
        grid.append(row)


visible = 0

def check_tree(x, y):
    height = grid[x][y]
    highest_from_left = grid[0][y]
    highest_from_right = grid[len(grid) - 1][y]
    highest_from_down = grid[x][len(grid) - 1]
    highest_from_top = grid[x][0]
    for i in range(x):
        if grid[i][y] > highest_from_left:
            highest_from_left = grid[i][y]
    for i in range(len(grid) - x - 1):
        if grid[len(grid) - i - 1][y] > highest_from_right:
            highest_from_right = grid[len(grid) - i - 1][y]
    for i in range(y):
        if grid[x][i] > highest_from_top:
            highest_from_top = grid[x][i]
    for i in range(len(grid) - y - 1):
        if grid[x][len(grid) - i - 1] > highest_from_down:
            highest_from_down = grid[x][len(grid) - i - 1]
    return height > highest_from_down or height > highest_from_left or height > highest_from_top or height > highest_from_right

for x in range(len(grid)):
    for y in range(len(grid)):
        if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid) - 1:
            visible += 1
        elif check_tree(x, y):
            visible += 1

# Task A
print(visible) 

def calculate_scenic_score(x, y):
    score = 0
    total_score = 1
    height = grid[x][y]
    for i in range(1, x + 1):
        score += 1
        if grid[x - i][y] >= height:
            break
    if score > 0:
        total_score *= score
    score = 0
    for i in range(1, y + 1):
        score += 1
        if grid[x][y - i] >= height:
            break
    if score > 0:
        total_score *= score
    score = 0
    for i in range(x + 1, len(grid)):
        score += 1
        if grid[i][y] >= height:
            break
    if score > 0:
        total_score *= score
    score = 0
    for i in range(y + 1, len(grid)):
        score += 1
        if grid[x][i] >= height:
            break
    if score > 0:
        total_score *= score
    return total_score

max_scenic_score = 0

for x in range(len(grid)):
    for y in range(len(grid)):
        score = calculate_scenic_score(x, y)
        if score > max_scenic_score:
            max_scenic_score = score

# Task B
print(max_scenic_score)