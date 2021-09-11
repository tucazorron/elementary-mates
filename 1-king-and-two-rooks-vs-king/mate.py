from colorama import Fore, Back, Style

positions = [[] for i in range(4)]
black_king = 0
white_king = 1
rook1 = 2
rook2 = 3
table = [[i for i in range(8)] for j in range(8)]
check_mate = False


def initialize_table():
    for i in range(8):
        for j in range(8):
            table[i][j] = "."


def transform_input_to_coordinates(index):
    positions[index][0] = chr(ord(positions[index][0].upper()) - 16)
    positions[index] = list(map(int, positions[index]))
    print(positions)


def get_initial_positions():
    positions[0] = [char for char in input("black king initial position: ")]
    positions[1] = [char for char in input("white king initial position: ")]
    positions[2] = [char for char in input("first rook initial position: ")]
    positions[3] = [char for char in input("second rook initial position: ")]
    for i in range(4):
        transform_input_to_coordinates(i)


def add_positions_to_table():
    for i in range(4):
        break


def get_square_color(i, j, counter):
    if counter % 2 == 0:
        print(Back.LIGHTGREEN_EX, end="")
    else:
        print(Back.GREEN, end="")


def print_table():
    square_counter = 0
    print(Back.WHITE + Fore.BLACK+ "                     " + Style.RESET_ALL)
    for i in range(8):
        print(Back.WHITE, end="")
        print(Fore.BLACK, end="")
        print(f" {8 - i} ", end="")
        for j in range(8):
            get_square_color(i, j, square_counter)
            square_counter += 1
            print(table[i][j], end=" ")
        square_counter += 1
        print(Back.WHITE + Fore.BLACK + "  " + Style.RESET_ALL)
    print(Back.WHITE + Fore.BLACK + "   A B C D E F G H   " + Style.RESET_ALL)


def get_black_move():
    black_move = [char for char in input("black king move: ")]
    transform_input_to_coordinates(0)


def play():
    initialize_table()
    # get_initial_positions()
    # add_positions_to_table()
    while not check_mate:
        print_table()
        # get_black_move()
        break


play()
