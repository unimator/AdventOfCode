def compare(l, r):
    if type(l) == type(r) and type(l) == int:
        if l < r:
            return -1
        elif l == r:
            return 0
        else:
            return 1
    
    if type(l) == type(r) and type(l) == type([]):
        i = 0
        while True:
            if i == len(l) and len(l) == len(r):
                return 0
            if i == len(l):
                return -1
            if i == len(r):
                return 1
            comp_res = compare(l[i], r[i])
            if comp_res == 0:
                i += 1
            else:
                return comp_res
    
    if type(l) == int and type(r) == type([]):
        return compare([l], r)

    if type(r) == int and type(l) == type([]):
        return compare(l, [r])

    raise ValueError("Out of range")

with open('input', 'r') as input_file:
    groups = input_file.read().split('\n\n')

    pair_counter = 0
    correct_pairs = []

    for group in groups:
        pair_counter += 1
        [left_str, right_str] = group.split('\n')
        [left, right] = [eval(left_str.strip()), eval(right_str.strip())]
        if compare(left, right) == -1:
            correct_pairs.append(pair_counter)
    
    # Task A
    print(sum(correct_pairs))

with open('input', 'r') as input_file:
    lines = [eval(line) for line in input_file if line != '\n']
    l2 = [[2]]
    l6 = [[6]]
    lines.append(l2)
    lines.append(l6)

    lines.sort(cmp=compare)

    # Task B
    print((lines.index(l2) + 1) * (lines.index(l6) + 1))