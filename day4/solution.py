class Range:
    def __init__(self, range_str):
        [beginning_str, end_str] = range_str.split('-')
        [beginning, end] = [int(beginning_str), int(end_str)]
        self.beginning = beginning
        self.end = end
    def contains(self, other):
        if self.beginning <= other.beginning and self.end >= other.end:
            return True
        else:
            return False
    def overlaps(self, other):
        if self.beginning <= other.end and self.beginning >= other.beginning:
            return True
        elif self.end <= other.end and self.end >= other.beginning:
            return True
        else:
            return False

sum_a = 0
sum_b = 0
with open('input', 'r') as input_file:
    lines = [line for line in input_file]
    for line in lines:
        [left_range_str, right_range_str] = line.split(',')
        [left_range, right_range] = [Range(left_range_str), Range(right_range_str)]
        if left_range.contains(right_range) or right_range.contains(left_range):
            sum_a += 1
        if left_range.overlaps(right_range) or right_range.overlaps(left_range):
            sum_b += 1

# Task A
print(sum_a)

# Task B
print(sum_b)

