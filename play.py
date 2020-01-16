import variables
from board import show_board, update_board
from win import check_win, win


def play():
    while not variables.finish:
        if variables.curPlayer == 1:
            variables.curChess = "*"
            print("\033[1;37;40m * - Enter the coords of the chess (e.g. A0): \033[0m")
        else:
            variables.curChess = "o"
            print("\033[1;30;42m o - Enter the coords of the chess (e.g. A0): \033[0m")
        user_input = input()
        ch = user_input[0]
        x = ord(ch.upper()) - 65
        y = int(user_input[1])
        if exist(x, y) and len(user_input) == 2:
            flag = update_board(x, y)
            if flag == 0:
                print("\033[31m****** The place has been taken! Please try again! \033[0m")
                continue
            f = check_win(x, y)
            if f == 1:
                win()
                break
            swap_player()
            show_board()
        else:
            print("\033[31m*** Invalid coords! Please try again! ***\033[0m")


def swap_player():
    variables.curPlayer *= -1


def exist(x, y):
    return 0 <= x < 10 and 0 <= y < 10

