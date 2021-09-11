white_king = []
black_king = []
rook1 = []
rook2 = []
table = [[i for i in range(8)] for j in range(8)]
check_mate = False


def initialize_table():
    for i in range(8):
        for j in range(8):
            table[i][j] = "."


def initial_positions():
    white_king = [char for char in input("white king initial position: ")]
    black_king = [char for char in input("black king initial position: ")]
    rook1 = [char for char in input("first rook initial position: ")]
    rook2 = [char for char in input("second rook initial position: ")]


def print_table():
    print("------------------- ")
    for i in range(8):
        print("|", end=" ")
        for j in range(8):
            print(table[i][j], end=" ")
        print("|")
    print("-------------------")


def play():
    initialize_table()
    # initial_positions()
    while not check_mate:
        print_table()
        break


play()
