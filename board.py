from variables import board
import variables


def init_board():
    for i in range(10):
        board.append([])
        for j in range(10):
            board[i].append('-')


def show_board():
    print('\033[1;30;46m------------------------------------------------')
    print('\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9')
    for i in range(len(board)):
        print(chr(i + ord('A')), end='\t')
        for j in range(len(board[i])):
            print(board[i][j], end='\t')
        print('\n')
    print('------------------------------------------------\n\033[0m')


def update_board(x, y):
    if board[x][y] == "-":
        if variables.curPlayer == 1:
            board[x][y] = "*"
        else:
            board[x][y] = "o"
        return 1
    else:
        return 0
