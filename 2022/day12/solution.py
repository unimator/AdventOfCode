grid = []

inf = 999999999999999

class Node:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
        self.color = 'white'
        self.dist = inf
        self.parent = None

S = (0, 20) # got from input file
E = (58, 20)

with open('input', 'r') as input_file:
    for line in input_file:
        grid.append([letter for letter in line.strip()])

grid[S[1]][S[0]] = 'a'
grid[E[1]][E[0]] = 'z'
width = len(grid[0])
height = len(grid)

def bfs(Start):
    nodes = []
    queue = []
    End = E
    for h in range(len(grid)):
        row = []
        for w in range(len(grid[0])):
            row.append(Node(w, h, grid[h][w]))
        nodes.append(row)
    nodes[Start[1]][Start[0]].color = 'gray'
    nodes[Start[1]][Start[0]].dist = 0
    nodes[Start[1]][Start[0]].parent = None
    queue.append([Start[1], Start[0]])

    def get_neighbours(x_p, y_p):
        current_value = ord(grid[y_p][x_p])
        if x_p > 0 and ord(grid[y_p][x_p - 1]) - 1 <= current_value:
            yield [x_p - 1, y_p]
        if y_p > 0 and ord(grid[y_p - 1][x_p]) - 1 <= current_value:
            yield [x_p, y_p - 1]
        if x_p < width - 1 and ord(grid[y_p][x_p + 1]) - 1 <= current_value:
            yield [x_p + 1, y_p]
        if y_p < height - 1 and ord(grid[y_p + 1][x_p]) - 1 <= current_value:
            yield [x_p, y_p + 1]

    while queue:
        [y, x] = queue.pop(0)
        for [n_x, n_y] in get_neighbours(x, y):
            if nodes[n_y][n_x].color == 'white':
                nodes[n_y][n_x].color = 'gray'
                nodes[n_y][n_x].dist = nodes[y][x].dist + 1
                nodes[n_y][n_x].parent = nodes[y][x]
                queue.append([n_y, n_x])
        nodes[y][x].color = 'black'

    return nodes[End[1]][End[0]].dist
    
# Task A
print(bfs(S))

best_bfs_b = 999999999
for h in range(len(grid)):
    for w in range(len(grid[0])):
        if grid[h][w] == 'a':
            bfs_val = bfs((w, h))
            if bfs_val < best_bfs_b:
                best_bfs_b = bfs_val

# Task B
print(best_bfs_b)