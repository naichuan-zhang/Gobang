import board
import variables


def check_win(x, y):
    # 上方
    if y >= 4:
        if variables.board[x][y - 1] == variables.curChess \
                and variables.board[x][y - 2] == variables.curChess \
                and variables.board[x][y - 3] == variables.curChess \
                and variables.board[x][y - 4] == variables.curChess:
            variables.finish = True
            win()
            return 1
    # 下方
    if y <= 5:
        if variables.board[x][y + 1] == variables.curChess \
                and variables.board[x][y + 2] == variables.curChess \
                and variables.board[x][y + 3] == variables.curChess \
                and variables.board[x][y + 4] == variables.curChess:
            variables.finish = True
            win()
            return 1
    # 左侧
    if x >= 4:
        if variables.board[x - 1][y] == variables.curChess \
                and variables.board[x - 2][y] == variables.curChess \
                and variables.board[x - 3][y] == variables.curChess \
                and variables.board[x - 4][y] == variables.curChess:
            variables.finish = True
            win()
            return 1
    # 右侧
    if x <= 5:
        if variables.board[x + 1][y] == variables.curChess \
                and variables.board[x + 2][y] == variables.curChess \
                and variables.board[x + 3][y] == variables.curChess \
                and variables.board[x + 4][y] == variables.curChess:
            variables.finish = True
            win()
            return 1
    # 左上
    if x <= 5 and y >= 4:
        if variables.board[x + 1][y - 1] == variables.curChess \
                and variables.board[x + 2][y - 2] == variables.curChess \
                and variables.board[x + 3][y - 3] == variables.curChess \
                and variables.board[x + 4][y - 4] == variables.curChess:
            variables.finish = True
            win()
            return 1
    # 左下
    if x >= 4 and y <= 5:
        if variables.board[x - 1][y + 1] == variables.curChess \
                and variables.board[x - 2][y + 2] == variables.curChess \
                and variables.board[x - 3][y + 3] == variables.curChess \
                and variables.board[x - 4][y + 4] == variables.curChess:
            variables.finish = True
            win()
            return 1
    # 右上
    if x >= 4 and y >= 4:
        if variables.board[x - 1][y - 1] == variables.curChess \
                and variables.board[x - 2][y - 2] == variables.curChess \
                and variables.board[x - 3][y - 3] == variables.curChess \
                and variables.board[x - 4][y - 4] == variables.curChess:
            variables.finish = True
            win()
            return 1
    # 右下
    if x <= 5 and y <= 5:
        if variables.board[x + 1][y + 1] == variables.curChess \
                and variables.board[x + 2][y + 2] == variables.curChess \
                and variables.board[x + 3][y + 3] == variables.curChess \
                and variables.board[x + 4][y + 4] == variables.curChess:
            variables.finish = True
            win()
            return 1


def win():
    """
    print out the final board and show a message to winner
    """
    print("The final board is shown below:")
    board.show_board()
    if variables.curPlayer == 1:
        print("\033[32m * has won the game! ***\033[0m")
    else:
        print("\033[32m o has won the game! ***\033[0m")
