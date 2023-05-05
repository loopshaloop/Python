import re
import enum
from copy import deepcopy
import os
import time

def clear():
    os.system('cls')

class Chess(enum.Enum):
    PAWN = 0
    ROOK = 1
    BISHOP = 2
    HORSE = 3
    QUEEN = 4
    KING = 5
    WHITE = True
    BLACK = False
    BOARD_WIDTH = 8
    LEGAL_CHARS = "abcdefgh"
    START_FEN = "RHBQKBHR/PPPPPPPP/8/8/8/8/pppppppp/rhbqkbhr w KQkq - 0 1"

def play():
    clear()
    print("This is not ready! Try it again later!")
    time.sleep(3)
    clear()
    exit()

def menu():
    print("To start playing, type \'play\'!\nTo quit, type \'quit\'!\nFor a tutorial, enter \'tutorial\'!")
    inp = input()
    match(inp):
        case "play":
            play()
        case "quit":
            print("Quitting!")
            time.sleep(2)
            clear()
            exit()
        case "tutorial":
            clear()
            print("This is a tutorial for this private version of chess!")
            print("")
            print("To start playing, type \'play\'!\nTo quit, type \'quit\'!\nTo go back to the menu, enter \'menu\'!")
            choice = input()
            if choice == "menu":
                return 1
        case _:
            print("Sorry, this is an unknown command!\n Please try again!")
            time.sleep(3)
            clear()
            return 1

def start_up():
    clear()
    print("Hello! Welcome to Chess!")
    time.sleep(3)
    clear()
    print("This is an exprimental version\nof the classic chess game I made!")
    time.sleep(3)
    clear()
    choice = menu()
    while choice == 1:
        choice = menu()

start_up()