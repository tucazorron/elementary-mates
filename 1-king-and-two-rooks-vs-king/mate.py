from os import system
from colorama import Fore, Back, Style

positions = [[] for i in range(4)]
last_positions = [[] for i in range(4)]
pieces = ["k", "K", "R", "R"]
# black king = 0
# white king = 1
# first rook = 2
# second rook = 3
table = [[i for i in range(8)] for j in range(8)]
check_mate = False
check = False


def print_title():
    system("clear")
    print("\n  King and Two Rooks vs King")
    input("\n  Press ENTER: ")


def initialize_table():
    for i in range(8):
        for j in range(8):
            table[i][j] = " "


def transform_input_to_coordinates(index):
    positions[index][0] = chr(ord(positions[index][0].upper()) - 16)
    positions[index] = list(map(int, positions[index]))


def get_initial_positions():
    system("clear")
    print("\n  Initial Positions")
    positions[0] = [coordinate for coordinate in input("\n  Black King: ")]
    positions[1] = [coordinate for coordinate in input("\n  White King: ")]
    positions[2] = [coordinate for coordinate in input("\n  First Rook: ")]
    positions[3] = [coordinate for coordinate in input("\n  Second Rook: ")]
    for index in range(4):
        transform_input_to_coordinates(index)
        last_positions[index] = positions[index]


def move_piece(index):
    rank = positions[index][0]
    file = positions[index][1]
    last_rank = last_positions[index][0]
    last_file = last_positions[index][1]
    table[last_rank - 1][last_file - 1] = " "
    table[rank - 1][file - 1] = pieces[index]
    last_positions[index] = positions[index]


def initialize_pieces_to_table():
    for index in range(4):
        move_piece(index)


def print_table_top_border():
    print("\n  " + Back.WHITE + Fore.BLACK +
          "                        " + Style.RESET_ALL)
    print("  " + Back.WHITE + Fore.BLACK +
          "                        " + Style.RESET_ALL)


def print_table_rank_coordinates(rank):
    print("  " + Back.WHITE + Fore.BLACK + f"  {rank} ", end="")


def get_square_color(square_counter):
    if square_counter % 2 == 0:
        print(Back.LIGHTMAGENTA_EX, end="")
    else:
        print(Back.MAGENTA, end="")


def print_table_square(rank, file):
    if table[file - 1][rank - 1] == "k":
        print(Fore.BLACK, end="")
    else:
        print(Fore.WHITE, end="")
    print(table[file - 1][rank - 1], end=" ")


def print_table_right_border():
    print(Back.WHITE + Fore.BLACK + "    " + Style.RESET_ALL)


def print_table_files_coordinates():
    print("  " + Back.WHITE + Fore.BLACK +
          "    A B C D E F G H     " + Style.RESET_ALL)
    print("  " + Back.WHITE + Fore.BLACK +
          "                        " + Style.RESET_ALL)


def print_table():
    system("clear")
    square_counter = 0
    print_table_top_border()
    for rank in range(8, 0, -1):
        print_table_rank_coordinates(rank)
        for file in range(1, 9):
            get_square_color(square_counter)
            square_counter += 1
            print_table_square(rank, file)
        square_counter += 1
        print_table_right_border()
    print_table_files_coordinates()
    print(f"\n  {positions}")


def get_black_move():
    positions[0] = [coordinate for coordinate in input("\n  Your move: ")]
    transform_input_to_coordinates(0)
    move_piece(0)


# def make_white_move():


def print_check_mate():
    print("\n  Check Mate: White is victorious.\n")


def play():
    print_title()
    initialize_table()
    get_initial_positions()
    initialize_pieces_to_table()
    while not check_mate:
        print_table()
        get_black_move()
        # make_white_move()
        # check_mate = True
    print_check_mate()


play()
