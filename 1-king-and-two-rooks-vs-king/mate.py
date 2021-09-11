from os import system
from colorama import Fore, Back, Style

positions = [[] for i in range(4)]
# black king = 0
# white king = 1
# first rook = 2
# second rook = 3
table = [[i for i in range(8)] for j in range(8)]
check_mate = False


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
    positions[0] = [i for i in input("\n  Black King: ")]
    positions[1] = [i for i in input("\n  White King: ")]
    positions[2] = [i for i in input("\n  First Rook: ")]
    positions[3] = [i for i in input("\n  Second Rook: ")]
    for i in range(4):
        transform_input_to_coordinates(i)


def add_positions_to_table():
    for i in range(4):
        break


def print_table_top_border():
    print("\n  " + Back.WHITE + Fore.BLACK +
          "                        " + Style.RESET_ALL)
    print("  " + Back.WHITE + Fore.BLACK +
          "                        " + Style.RESET_ALL)


def print_table_rank_coordinates(rank):
    print("  " + Back.WHITE + Fore.BLACK + f"  {rank} ", end="")


def get_square_color(square_counter):
    if square_counter % 2 == 0:
        print(Back.LIGHTGREEN_EX, end="")
    else:
        print(Back.GREEN, end="")


def print_table_square(rank, file):
    print(table[rank - 1][file - 1], end=" ")


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


def get_black_move():
    positions[0] = [char for char in input("\n  Your move: ")]
    transform_input_to_coordinates(0)


def play():
    print_title()
    initialize_table()
    get_initial_positions()
    add_positions_to_table()
    while not check_mate:
        print_table()
        # get_black_move()
        break


play()
