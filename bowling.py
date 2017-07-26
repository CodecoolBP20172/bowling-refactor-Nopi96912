def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for turn in range(len(game)):
        if game[turn] == '/':
            result += 10 - last
        else:
            result += get_value(game[turn])
        result += add_result(game, turn, frame)
        last = get_value(game[turn])
        if not in_first_half:
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
        if game[turn] == 'X' or game[turn] == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    not_numbers = ['X', 'x', '/']
    if char in numbers:
        return int(char)
    elif char in not_numbers:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def add_result(string, index, frame):
    result = 0
    if frame < 10 and get_value(string[index]) == 10:
        if string[index] == '/':
            result += get_value(string[index+1])
        elif string[index] == 'X' or string[index] == 'x':
            result += get_value(string[index+1])
            if string[index+2] == '/':
                result += 10 - get_value(string[index+1])
            else:
                result += get_value(string[index+2])
    return result
