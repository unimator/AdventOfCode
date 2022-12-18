import re

pattern = r'(\d+),(\d+),(\d+)'

POND_SIZE = 22

with open('input', 'r') as input_file:
    cubes = []
    for line in input_file:
        [x, y, z] = re.search(pattern, line).groups()
        cubes.append([int(x), int(y), int(z)])
    
    task_a_result = 0
    for [cx, cy, cz] in cubes:
        faces_not_covered = 6
        for [ox, oy, oz] in cubes:
            if cx == ox and cy == oy and cz == oz:
                continue
            if cx == ox and cy == oy and abs(cz - oz) == 1:
                faces_not_covered -= 1
            if cx == ox and abs(cy - oy) == 1 and cz == oz:
                faces_not_covered -= 1
            if abs(cx - ox) == 1 and cy == oy and cz == oz:
                faces_not_covered -= 1
            
        task_a_result += faces_not_covered
    
    print(task_a_result)

    pond = [[[False for _ in range(POND_SIZE)] for _ in range(POND_SIZE)] for _ in range(POND_SIZE)]

    def cool(target):
        pond[target[0]][target[1]][target[2]] = True

    def get_neighbours_to_cool(current):
        [x, y, z] = current
        result = []
        if x > 0 and not pond[x-1][y][z] and [x-1, y, z] not in cubes:
            result.append([x-1, y, z])
        if y > 0 and not pond[x][y-1][z] and [x, y-1, z] not in cubes:
            result.append([x, y-1, z])
        if z > 0 and not pond[x][y][z-1] and [x, y, z-1] not in cubes:
            result.append([x, y, z-1])
        if x < POND_SIZE - 1 and not pond[x+1][y][z] and [x+1, y, z] not in cubes:
            result.append([x+1, y, z])
        if y < POND_SIZE - 1 and not pond[x][y+1][z] and [x, y+1, z] not in cubes:
            result.append([x, y+1, z])
        if z < POND_SIZE - 1 and not pond[x][y][z+1] and [x, y, z+1] not in cubes:
            result.append([x, y, z+1])
        return result

    current_to_cool = [0, 0, 0]
    Q = [current_to_cool]
    while len(Q) > 0:
        c = Q.pop()
        cool(c)
        Q.extend(get_neighbours_to_cool(c))

    task_b_result = 0
    for [cx, cy, cz] in cubes:
        faces_not_covered = 6
        for [ox, oy, oz] in cubes:
            if cx == ox and cy == oy and cz == oz:
                continue
            if cx == ox and cy == oy and abs(cz - oz) == 1:
                faces_not_covered -= 1
            if cx == ox and abs(cy - oy) == 1 and cz == oz:
                faces_not_covered -= 1
            if abs(cx - ox) == 1 and cy == oy and cz == oz:
                faces_not_covered -= 1

        x = cx
        y = cy
        z = cz
        if x - 1 > 0 and pond[x-1][y][z] == False and [x-1,y,z] not in cubes:
            faces_not_covered -= 1
        if y - 1 > 0 and pond[x][y-1][z] == False and [x,y-1,z] not in cubes:
            faces_not_covered -= 1
        if z - 1 > 0 and pond[x][y][z-1] == False and [x,y,z-1] not in cubes:
            faces_not_covered -= 1
        if pond[x+1][y][z] == False and [x+1,y,z] not in cubes:
            faces_not_covered -= 1
        if pond[x][y+1][z] == False and [x,y+1,z] not in cubes:
            faces_not_covered -= 1
        if pond[x][y][z+1] == False and [x,y,z+1] not in cubes:
            faces_not_covered -= 1


        task_b_result += faces_not_covered
    
    print(task_b_result)
