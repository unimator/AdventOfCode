CAVE_WIDTH = 7
CAVE_HEIGHT = 100000

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape1:
    def __init__(self, bottom_line):
        self.__spawn(bottom_line)
        
    def __spawn(self, bottom_line):
        self.position = Position(2, bottom_line + 3)

    def try_fall(self, array):
        if self.position.y > 0 and all(array[self.position.y - 1][self.position.x + l] == '.' for l in range(4)):
            self.position.y -= 1
            return True
        else:
            return False
    
    def try_move_right(self, array):
        if self.position.x + 4 < CAVE_WIDTH and array[self.position.y][self.position.x + 4] == '.':
            self.position.x += 1
            return True
        else:
            return False

    def try_move_left(self, array):
        if self.position.x > 0 and array[self.position.y][self.position.x - 1] == '.':
            self.position.x -= 1
            return True
        else:
            return False

    def rest(self, array):
        for i in range(4):
            array[self.position.y][self.position.x + i] = '1'

class Shape2:
    def __init__(self, bottom_line):
        self.__spawn(bottom_line)
        
    def __spawn(self, bottom_line):
        self.position = Position(2, bottom_line + 5)

    def try_fall(self, array):
        if self.position.y > 2 and array[self.position.y - 2][self.position.x] == '.' and \
            array[self.position.y - 3][self.position.x + 1] == '.' and \
            array[self.position.y - 2][self.position.x + 2] == '.':
            self.position.y -= 1
            return True
        else:
            return False
    
    def try_move_right(self, array):
        if self.position.x + 3 < CAVE_WIDTH and array[self.position.y][self.position.x + 2] == '.' and \
            array[self.position.y - 1][self.position.x + 3] == '.' and \
            array[self.position.y - 2][self.position.x + 2] == '.':
            self.position.x += 1
            return True
        else:
            return False

    def try_move_left(self, array):
        if self.position.x > 0 and array[self.position.y][self.position.x] == '.' and \
            array[self.position.y - 1][self.position.x - 1] == '.' and \
            array[self.position.y - 2][self.position.x] == '.':
            self.position.x -= 1
            return True
        else:
            return False

    def rest(self, array):
        for i in range(3):
            array[self.position.y - 1][self.position.x + i] = '2'
            array[self.position.y - i][self.position.x + 1] = '2'

class Shape3:
    def __init__(self, bottom_line):
        self.__spawn(bottom_line)
        
    def __spawn(self, bottom_line):
        self.position = Position(2, bottom_line + 5)

    def try_fall(self, array):
        if self.position.y > 2 and all(array[self.position.y - 3][self.position.x + l] == '.' for l in range(3)):
            self.position.y -= 1
            return True
        else:
            return False
    
    def try_move_right(self, array):
        if self.position.x + 3 < CAVE_WIDTH and all(array[self.position.y - i][self.position.x + 3] == '.' for i in range(3)):
            self.position.x += 1
            return True
        else:
            return False

    def try_move_left(self, array):
        if self.position.x > 0 and array[self.position.y][self.position.x + 1] == '.' and \
            array[self.position.y - 1][self.position.x + 1] == '.' == '.' and \
            array[self.position.y - 2][self.position.x - 1] == '.':
            self.position.x -= 1
            return True
        else:
            return False

    def rest(self, array):
        for i in range(3):
            array[self.position.y - i][self.position.x + 2] = '3'
            array[self.position.y - 2][self.position.x + i] = '3'

class Shape4:
    def __init__(self, bottom_line):
        self.__spawn(bottom_line)
        
    def __spawn(self, bottom_line):
        self.position = Position(2, bottom_line + 6)

    def try_fall(self, array):
        if self.position.y > 3 and array[self.position.y - 4][self.position.x] == '.':
            self.position.y -= 1
            return True
        else:
            return False
    
    def try_move_right(self, array):
        if self.position.x + 1 < CAVE_WIDTH and all(array[self.position.y - i][self.position.x + 1] == '.' for i in range(4)):
            self.position.x += 1
            return True
        else:
            return False

    def try_move_left(self, array):
        if self.position.x > 0 and all(array[self.position.y - i][self.position.x - 1] == '.' for i in range(4)):
            self.position.x -= 1
            return True
        else:
            return False

    def rest(self, array):
        for i in range(4):
            array[self.position.y - i][self.position.x] = '4'

class Shape5:
    def __init__(self, bottom_line):
        self.__spawn(bottom_line)
        
    def __spawn(self, bottom_line):
        self.position = Position(2, bottom_line + 4)

    def try_fall(self, array):
        if self.position.y > 1 and all(array[self.position.y - 2][self.position.x + i] == '.' for i in range(2)):
            self.position.y -= 1
            return True
        else:
            return False
    
    def try_move_right(self, array):
        if self.position.x + 2 < CAVE_WIDTH and all(array[self.position.y - i][self.position.x + 2] == '.' for i in range(2)):
            self.position.x += 1
            return True
        else:
            return False

    def try_move_left(self, array):
        if self.position.x > 0 and all(array[self.position.y - i][self.position.x - 1] == '.' for i in range(2)):
            self.position.x -= 1
            return True
        else:
            return False

    def rest(self, array):
        for i in range(2):
            array[self.position.y - i][self.position.x] = '5'
            array[self.position.y - i][self.position.x + 1] = '5'

bottom_line = 0

def generate_rock():
    while True:
        yield Shape1(bottom_line)
        yield Shape2(bottom_line)
        yield Shape3(bottom_line)
        yield Shape4(bottom_line)
        yield Shape5(bottom_line)

rocks_to_simulate = 10000
TASK_A_SIZE = 2022
TASK_B_SIZE = 1000000000000

def print_cave():
    for i in reversed(range(bottom_line + 6)):
        print(''.join(cave[i]))

jets_dict = {}

def bottom_lines_str(size):
    return ''.join([''.join([c for c in cave[bottom_line - i - 1]]) for i in range(size)])

with open('day17\input', 'r') as input_file:
    predicted_repeat_size = 100
    jets = [c for c in input_file.read()]
    rocks_generator = generate_rock()
    jet_it = 0
    cave = [['.' for _ in range(CAVE_WIDTH)] for _ in range(CAVE_HEIGHT)]
    task_b_result = None
    
    first_repeat_shape = None
    first_repeat_line = 0
    first_repeat_num_of_items_dropped = 0
    first_jet = None
    first_full_hash = None

    second_repeat_line = 0
    second_repeat_num_of_items_dropped = 0

    additional_height_for_b_task = 0
    left_to_drop = None
    b_solution_found_flag = False

    repeat_patterns = set()

    for i in range(rocks_to_simulate):
        rock = next(rocks_generator)
        jet_it_rounded = jet_it % len(jets)
        if left_to_drop != None:
            if left_to_drop == 0:
                additional_height_for_b_task = bottom_line - second_repeat_line
                b_solution_found_flag = True
            left_to_drop -= 1
        if bottom_line > predicted_repeat_size:
            bottom_line_hash = bottom_lines_str(predicted_repeat_size)
            full_hash = str(type(rock)) + '_' + str(jet_it_rounded) + '_' + bottom_line_hash
            if full_hash not in repeat_patterns:
                repeat_patterns.add(full_hash)
            else:
                if first_repeat_shape is None:
                    first_repeat_shape = str(type(rock))
                    first_repeat_line = bottom_line
                    first_repeat_num_of_items_dropped = i
                    first_full_hash = full_hash
                elif first_repeat_shape == str(type(rock)) and first_full_hash == full_hash:
                    second_repeat_line = bottom_line
                    second_repeat_num_of_items_dropped = i
                    repeat_items_count = second_repeat_num_of_items_dropped - first_repeat_num_of_items_dropped

                    repeat_height = second_repeat_line - first_repeat_line
                    non_repeated_items = i % repeat_items_count
                    non_repeated_height = second_repeat_line

                    # [dropped without pattern]  [pattern] [pattern] [pattern] ... [pattern]  [rest]
                    #    non_repeated_height       rocks left to drop * pattern_height      left_to_drop
                    task_b_result = non_repeated_height + ((TASK_B_SIZE - i) // repeat_items_count) * repeat_height
                    if left_to_drop == None:
                        left_to_drop = TASK_B_SIZE - non_repeated_items - ((TASK_B_SIZE - non_repeated_items) // repeat_items_count) * repeat_items_count

        while True:
            jet = jets[jet_it % len(jets)]
            jet_it += 1
            if jet == '<':
                rock.try_move_left(cave)
            elif jet == '>':
                rock.try_move_right(cave)
            else:
                raise ValueError('Uknown jet %s' % jet)
            
            if not rock.try_fall(cave):
                break
        rock.rest(cave)
        while True:
            cave_row = cave[bottom_line]
            if all([cave_row[i] == '.' for i in range(CAVE_WIDTH)]):
                break
            else:
                bottom_line += 1

        if i == TASK_A_SIZE:
            # Task A
            print(bottom_line - 1)
        
        if b_solution_found_flag and i > TASK_A_SIZE:
            # Task B
            break
    
    task_b_result += additional_height_for_b_task - 1 # -1 because we're looking for structure height, not first full line free above which was used to calculate spawn position
    print(task_b_result)
