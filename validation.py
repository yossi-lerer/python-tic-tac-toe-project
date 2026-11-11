def is_empty(board, cell):
    for index_row, row in enumerate(board):
        for index, i in enumerate(row):
            if cell == i:
                if i != "X" and i != "O":
                    return True
    return False

def is_in_range(num):
    if 1 <= int(num) and int(num) <=9:
        return True 

def is_positive_number(num):
    try:
        int(num)
    except:
        return False
    return True