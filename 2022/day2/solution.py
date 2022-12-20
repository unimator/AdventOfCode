a_sum = 0
b_sum = 0

with open('input', 'r') as input_file:
    lines = [line for line in input_file]
    for line in lines:
        [they, us] = line.split(" ")
        they = they.strip()
        us = us.strip()
        
        a_symbol_score = 0
        b_symbol_score = 0

        if us == 'X':
            a_symbol_score = 1
        elif us == 'Y':
            a_symbol_score = 2
        elif us == 'Z':
            a_symbol_score = 3
        else:
            raise ValueError("Out of range")

        a_round_score = 0
        b_round_score = 0

        if they == 'A':
            if us == 'X':
                a_round_score = 3
                b_symbol_score = 3
            elif us == 'Y':
                a_round_score = 6
                b_round_score = 3
                b_symbol_score = 1
            elif us == 'Z':
                b_round_score = 6
                b_symbol_score = 2
        elif they == 'B':
            if us == 'X':
                b_symbol_score = 1
            if us == 'Y':
                a_round_score = 3
                b_round_score = 3
                b_symbol_score = 2
            elif us == 'Z':
                a_round_score = 6
                b_round_score = 6
                b_symbol_score = 3
            pass
        elif they == 'C':
            if us == 'X':
                a_round_score = 6
                b_symbol_score = 2
            elif us == 'Y':
                b_round_score = 3
                b_symbol_score = 3
            elif us == 'Z':
                a_round_score = 3
                b_round_score = 6
                b_symbol_score = 1
            pass
        else:
            raise ValueError("Out of range")
        
        a_sum += a_symbol_score + a_round_score
        b_sum += b_symbol_score + b_round_score
    
    # Task A
    print(a_sum)

    # Task B
    print(b_sum)

