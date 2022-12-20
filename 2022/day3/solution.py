def convert_to_priority(letter):
    if ord(letter) <= ord('Z') and ord(letter) >= ord('A'):
        return 26 + ord(letter) - ord('A') + 1
    else:
        return ord(letter) - ord('a') + 1

a_priorities_sum = 0
b_priorities_sum = 0
group_size = 3
with open('input', 'r') as input_file:
    lines = [line for line in input_file]
    for line in lines:
        line_length = len(line)
        half_length = int(line_length / 2)
        [left, right] = [line[:half_length], line[half_length:]]
        duplicates = []
        for cl in left:
            if  cl in right and cl not in duplicates:
                a_priorities_sum += convert_to_priority(cl)
                duplicates.append(cl)
    grouped_lines = [lines[n:n+group_size] for n in range(0, len(lines), group_size)]
    for [r1, r2, r3] in grouped_lines:
        for c1 in r1:
            if c1 in r2 and c1 in r3:
                b_priorities_sum += convert_to_priority(c1)
                break

# Task A
print(a_priorities_sum)

# Task B
print(b_priorities_sum)
