from board import create_board, cell_selection, check_win
from display import display_board
from user_input import user_num_input

def run_game():
    the_board = create_board()
    display_board(the_board)
    counter = 0
    player = "X"
    while True:
        if counter == 9:
            print("draw")
            break

        user_select = user_num_input(f"please select {player} ", the_board)
        the_board = cell_selection(the_board, user_select, player)
        display_board(the_board)
        counter += 1
        if check_win(the_board, player):
            print(f"{player} win")
            break

        player = "O" if player == "X" else "X"