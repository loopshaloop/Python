import re
import string
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
    BLACK = -1
    BOARD_WIDTH = 8
    LEGAL_CHARS = "abcdefgh"
    START_FEN = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr w KQkq - 0 1"


class Tile():
    def __init__(self, is_threatened = False, x = None, y = None):
        self.x = x
        self.y = y
        self.is_threatened = is_threatened

    def __repr__(self) -> str:
        ret = " "
        if self.x < 7:
            ret += "|"
        return ret
        

class Piece(Tile):
    def __init__(self, piece_type=None, color=None, has_moved=False, is_threatened=False, x=None, y=None):
        super().__init__(is_threatened, x, y)
        self.piece_type = piece_type
        self.color = color
        self.has_moved = has_moved
        self.possible_moves = []

class Game():
    def __init__(self, board = [], history = [], team_white = [], team_black = [], turn = True):
        self.board = board
        self.history = history
        self.team_white = team_white
        self.team_black = team_black
        self.turn = turn


    def NewBoard(self):
        for y in range(8):
            self.board.append([])
            for x in range(8):
                self.board[y].append(Tile(False,x,y))

        self.PrintBoard()


    def NewGame(self):
        self.history = ["RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr w KQkq - 0 1"]
        self.turn = True
        self.NewBoard()
        #self.Match()

    
    def CheckTeams(self):
        print("e")


    def FENToBoard(self):
        print("e")


    def BoardToFEN(self):
        print("e")

    
    def Match(self):
        teams = self.CheckTeams()
        white_team = teams[0]
        black_team = teams[1]
        while King() in white_team and King() in black_team:
            self.PrintBoard()

        print("e")


    def PrintBoard(self):
        #print("e")
        board_str = "  1 2 3 4 5 6 7 8\n"
        for y in range(8):
            board_str += Chess.LEGAL_CHARS.value[y] + " "
            if y < 7:
                board_str += '\x1B[4m'
            for x in range(8):
                board_str += self.board[y][x].__repr__()
            board_str += "\n"
            if y < 7:
                board_str += '\x1B[0m'
            
        print(board_str)

def Play():
    print("Starting a new game(default)")
    time.sleep(3)
    clear()
    game = Game()
    game.NewGame()
    """
    print("This is not ready! Try it again later!")
    time.sleep(3)
    clear()
    exit()
    """

def Menu():
    print("To start playing, type \'play\'!\nTo quit, type \'quit\'!\nFor a tutorial, enter \'tutorial\'!")
    inp = input()
    match(inp):
        case "play":
            Play()
        case "quit":
            print("Quitting!")
            time.sleep(2)
            clear()
            exit()
        case "tutorial":
            clear()
            print("This is a tutorial for this private version of chess!")
            print("")
            print("To start playing, type \'play\'!\nTo quit, type \'quit\'!\nTo go back to the Menu, enter \'Menu\'!")
            choice = input()
            if choice == "Menu":
                return 1
        case _:
            print("Sorry, this is an unknown command!\n Please try again!")
            time.sleep(3)
            clear()
            return 1


def StartUp():
    clear()
    print("Hello! Welcome to Chess!")
    time.sleep(3)
    clear()
    print("This is an exprimental version\nof the classic chess game I made!")
    time.sleep(3)
    clear()
    choice = Menu()
    while choice == 1:
        choice = Menu()


if __name__ == "__main__":
    StartUp()