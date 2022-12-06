def are_all_different(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] == arr[j]:
                return False
    return True

size = 14 # 4 for Task A, 14 for Task B - just switch it to get the result of the other task
with open('input') as input_file:
    line = input_file.readline()
    counter = 0
    buf = []
    for c in line:
        counter += 1
        if len(buf) < size:
            buf.append(c)
            continue
        del buf[0]
        buf.append(c)
        if are_all_different(buf):
            # Task A / B
            print(counter)
            break
        
