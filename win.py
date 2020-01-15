import board
from variables import curPlayer


def check_win():
    pass


def win():
    """
    print out the final board and show a message to winner
    """
    print("The final board is shown below:")
    board.show_board()
    if curPlayer == 1:
        print("\033[32m * has won the game! ***\033[0m")
    else:
        print("\033[32m o has won the game! ***\033[0m")
