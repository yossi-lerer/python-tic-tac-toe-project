def create_board():
    board = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    return board

def cell_selection(board, cell, player):
    for index_row, row in enumerate(board):
        for index, i in enumerate(row):
            if cell == i:
                board[index_row][index] = player
    return board

def check_win(board, player):
    WINNING_LINES = [
    ((0,0), (0,1), (0,2)),
    ((1,0), (1,1), (1,2)),
    ((2,0), (2,1), (2,2)),
    ((0,0), (1,0), (2,0)),
    ((0,1), (1,1), (2,1)),
    ((0,2), (1,2), (2,2)),
    ((0,0), (1,1), (2,2)),
    ((0,2), (1,1), (2,0))
    ]

    for wins in WINNING_LINES:
        player_win = False
        for win in wins:
            if board[win[0]][win[1]] == player:
                player_win = True
            else:                
                player_win = False
                break
        if player_win:
            return True
    