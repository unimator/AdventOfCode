import re

class File:
    def __init__(self, name, parent_dir, size):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir

class Directory:
    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir
        self.files = []
        self.subdirs = []

    def size(self):
        total_size = 0
        for file in self.files:
            total_size += file.size
        for dir in self.subdirs:
            total_size += dir.size()
        return total_size

root = Directory('/', None)
current = root
pattern_cd = "\$ cd (.+)"
pattern_dir = "dir ([a-z]+)"
pattern_file = "(\d+) ([a-z\.]+)"

def match_dir_name(name, dir):
    if dir.name == name:
        return True
    return False

with open('input', 'r') as input_file:
    for line in input_file:
        line = line.strip()
        cd_match = re.match(pattern_cd, line)
        dir_match = re.match(pattern_dir, line)
        file_match = re.match(pattern_file, line)
        if line == "$ cd /":
            current = root
        elif line == "$ ls":
            pass
        elif line == "$ cd ..":
            current = current.parent_dir
        elif cd_match != None:
            dir_name = cd_match.group(1)
            current = next(d for d in current.subdirs if match_dir_name(cd_match.group(1), d))
        elif dir_match != None:
            new_directory = Directory(dir_match.group(1), current)
            current.subdirs.append(new_directory)
        elif file_match != None:
            new_file = File(file_match.group(2), current, int(file_match.group(1)))
            current.files.append(new_file)
        else:
            raise ValueError('Out of range (%s)' % line)

disk_size = 70000000
update_size = 30000000
at_most_size = 100000
task_a_size = 0

def count_recursively(dir):
    total_size = dir.size()
    if dir.size() > at_most_size:
        total_size =  0
    for d in dir.subdirs:
        total_size += count_recursively(d)
    return total_size
        
task_a_size = count_recursively(root)

occupied_size = root.size()
free_size = disk_size - occupied_size
required_size = update_size - free_size

# Task A
print(task_a_size)

cur_smallest = root

def search_recursively(dir):
    global cur_smallest
    if dir.size() < cur_smallest.size() and dir.size() >= required_size:
        cur_smallest = dir
    for d in dir.subdirs:
        search_recursively(d)

search_recursively(cur_smallest)

# Task B
print(cur_smallest.size())