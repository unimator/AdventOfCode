import re

pattern = r'Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)'

YA=2000000
YB=YA * 2

coverage = [[] for _ in range(YB)]

def taxicab_distance(T1, T2):
    return sum([abs(t1 - t2) for (t1, t2) in zip(T1, T2)])

def update(i):
    for r1 in coverage[i]:
        [ex1_beg, ex1_end] = r1
        for r2 in coverage[i]:
            [ex2_beg, ex2_end] = r2
            if r1 == r2:
                continue
            if ex1_beg <= ex2_beg and ex1_end >= ex2_end:
                coverage[i].remove(r2)
                update(i)
                return
            elif ex1_beg >= ex2_beg and ex1_end <= ex2_end:
                coverage[i].remove(r1)
                update(i)
                return
            elif ex1_beg <= ex2_beg and ex1_end >= ex2_beg:
                coverage[i].remove(r1)
                coverage[i].remove(r2)
                coverage[i].append([ex1_beg, ex2_end])
                update(i)
                return
            elif ex1_beg <= ex2_end and ex1_beg >= ex2_beg:
                coverage[i].remove(r1)
                coverage[i].remove(r2)
                coverage[i].append([ex2_beg, ex1_end])
                update(i)
                return

def add_coverage(beg, end, i):
    for r in coverage[i]:
        [ex_beg, ex_end] = r
        if ex_beg == beg and ex_end == end:
            return
    coverage[i].append([beg, end])
    update(i)

with open('day15/input', 'r') as input_file:
    task_a_result = 0

    Ares = set()

    c = 0
    for line in input_file:
        sensor_x, sensor_y, beacon_x, beacon_y = re.search(pattern, line).groups()
        sensor_x, sensor_y, beacon_x, beacon_y = int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)
        distance = taxicab_distance([sensor_x, sensor_y], [beacon_x, beacon_y])
        
        if sensor_y > YA and sensor_y - distance < YA:
            expr = YA - sensor_y + distance
            for i in range(2 * expr):
                Ares.add(sensor_x - expr + i)
        if sensor_y < YA and sensor_y + distance > YA:
            expr = sensor_y + distance - YA
            for i in range(2 * expr):
                Ares.add(sensor_x - expr + i)
    
        for i in range(0, distance + 1):
            y_low = sensor_y + i - distance
            y_high = sensor_y - i + distance
            if y_low >= 0 and y_low < YB:
                beg = sensor_x - i
                end = sensor_x + i + 1
                add_coverage(beg, end, y_low)
            if y_high >= 0 and y_high < YB:
                beg = sensor_x - i
                end = sensor_x + i + 1
                add_coverage(beg, end, y_high)

        c += 1
    # Task A
    print(len(Ares))

    for i in range(YB):
        if len(coverage[i]) == 1:
            continue
        r1 = coverage[i][0]
        r2 = coverage[i][1]
        if r2[0] < r1[0]:
            r1 = r2
        # Task B 
        print(r1[1] * YA * 2 + i) # possibly the correct solution is given for r1[0] / r2[0] because ranges may be flipped
