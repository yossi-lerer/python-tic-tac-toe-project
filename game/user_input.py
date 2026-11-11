from game.validation import is_empty, is_in_range, is_positive_number
def user_num_input(msg, the_board):
    validate = False
    cell_input = ""
    while not validate:
        cell_input = input(msg)

        if is_positive_number(cell_input) and is_empty(the_board, int(cell_input)) and is_in_range(cell_input):
                validate = True

    return int(cell_input)