import re
import enum

#TODO: move rules + pat

class Chess(enum.Enum):
    PAWN = "p"
    ROOK = "r"
    BISHOP = "b"
    HORSE = "h"
    QUEEN = "q"
    KING = "k"
    WHITE = True
    BLACK = False
    BOARD_WIDTH = 8
    LEGAL_CHARS = "abcdefgh"
    START_FEN = "RHBQKBHR/PPPPPPPP/8/8/8/8/pppppppp/rhbqkbhr w KQkq - 0 1"
    
"""
This is the abstract class for the pieces.
The formula for the index is:
 x(numeral) + y(alphabetical) * width(of the board)
 We count each from 0.
 For example, a piece with the index of 20 is:
 4(x) + 2(y, also know as c) * 8(width of board) = 20(index)
 it is also known as c4
 The reverse formula is:
 x = index - y * 8
 y = (index - x) / 8 
"""

class Piece():
    def __init__(self, index = None, piece_type = None, color = None):
        self.index = index
        self.y = self.index / 8
        self.x = self.index % Chess.BOARD_WIDTH.value
        self.piece_type = piece_type
        self.color = color
        self.direction = None
        self.has_moved = None
        self.possible_moves = []
    
    def __repr__(self) -> str:
        str = self.piece_type.value
        if self.color == Chess.BLACK:
            str = str.upper() 
        return str


"""
This is the class for a pawn.
I made it inherently different from the other classes,
as it can move only forward.
I made it so it legal moves will be dependent on an attribute
called 'direction'.
The attribute is re-initalized during init according to
the pawn's color(white('True') is 1 as he is advancing down the
 board, and black('False') is -1 for the exact opposite reason).
"""

class Pawn(Piece):
    def __init__(self, index, piece_type, color):
        super().__init__(index, piece_type, color)
        self.has_moved = False
        if self.color == True:
            self.direction = 1
        else:
            self.direction = -1

    def move(self, up_end_index):
        self.possible_moves = []

        if up_end_index in self.possible_moves:
            game.board[self.index], game.board[up_end_index[0] + up_end_index[1]] = game.board[up_end_index[0] + up_end_index[1]], game.board[self.index]
            self.index = up_end_index[0] * Chess.BOARD_WIDTH.value + up_end_index[1]
            if self.color == Chess.BLACK:
                game.movesMade[0] + 1
            else:
                game.movesMade[1] + 1
            not game.turn

            game.boardToFEN()

        else:
            print("Illegal move! Please try again!")
            return False


class Rook(Piece):
    def __init__(self, index, piece_type, color):
        super().__init__(index, piece_type, color)
    
    def move(self, up_end_index):
        self.possible_moves = []

        if up_end_index in self.possible_moves:
            game.board[up_end_index[0], up_end_index[1]] = self
            game.board[self.x, self.y] = None
            self.index = up_end_index[0] * Chess.BOARD_WIDTH.value + up_end_index[1]
            if self.color == Chess.BLACK:
                game.movesMade[0] + 1
            else:
                game.movesMade[1] + 1
            not game.turn

            game.boardToFEN()

        else:
            print("Illegal move! Please try again!")
            return False


class Bishop(Piece):
    def __init__(self, index, piece_type, color):
        super().__init__(index, piece_type, color)
    
    def move(self, up_end_index):
        self.possible_moves = []

        if up_end_index in self.possible_moves:
            game.board[up_end_index[0], up_end_index[1]] = self
            game.board[self.x, self.y] = None
            self.index = up_end_index[0] * Chess.BOARD_WIDTH.value + up_end_index[1]
            if self.color == Chess.BLACK:
                game.movesMade[0] + 1
            else:
                game.movesMade[1] + 1
            not game.turn

            game.boardToFEN()

        else:
            print("Illegal move! Please try again!")
            return False

class Horse(Piece):
    def __init__(self, index, piece_type, color):
        super().__init__(index, piece_type, color)
    
    def move(self, up_end_index):
        self.possible_moves = []

        if up_end_index in self.possible_moves:
            game.board[up_end_index[0], up_end_index[1]] = self
            game.board[self.x, self.y] = None
            self.index = up_end_index[0] * Chess.BOARD_WIDTH.value + up_end_index[1]
            if self.color == Chess.BLACK:
                game.movesMade[0] + 1
            else:
                game.movesMade[1] + 1
            not game.turn

            game.boardToFEN()

        else:
            print("Illegal move! Please try again!")
            return False


class Queen(Piece):
    def __init__(self, index, piece_type, color):
        super().__init__(index, piece_type, color)
    
    def move(self, up_end_index):
        self.possible_moves = []

        if up_end_index in self.possible_moves:
            game.board[up_end_index[0], up_end_index[1]] = self
            game.board[self.x, self.y] = None
            self.index = up_end_index[0] * Chess.BOARD_WIDTH.value + up_end_index[1]
            if self.color == Chess.BLACK:
                game.movesMade[0] + 1
            else:
                game.movesMade[1] + 1
            not game.turn

            game.boardToFEN()

        else:
            print("Illegal move! Please try again!")
            return False


class King(Piece):
    def __init__(self, index, piece_type, color):
        super().__init__(index, piece_type, color)

    def move(self, up_end_index):
        self.possible_moves = []

        if up_end_index in self.possible_moves:
            game.board[up_end_index[0], up_end_index[1]] = self
            game.board[self.x, self.y] = None
            self.index = up_end_index[0] * Chess.BOARD_WIDTH.value + up_end_index[1]
            if self.color == Chess.BLACK:
                game.movesMade[0] + 1
            else:
                game.movesMade[1] + 1
            not game.turn

            game.boardToFEN()

        else:
            print("Illegal move! Please try again!")
            return False

"""
This is the abstract class for a game.
The save creation is not perfect as it is,
but it probably works well enough for now.
The FEN parser works 2 way, with parsing FEN string
to a printable list, and a printable list to a FEN
string(for saves).
The way to move pieces is to to write their current location
and their destined one, without commas, and alphabet first.
For example:
c4e5
Which means c4 to e5.
"""

class Game():
    def __init__(self):
        self.history = [Chess.START_FEN.value]
        self.FENstr = self.history[-1]
        self.board = self.FENToBoard()
        self.turn = True
        self.movesMade = [0, 1]
    
    def saveGame(self):
        c = 0
        while True:
            c + 1
            try:
                save = open(f"save{c}.txt", "r")
                save.close()
                continue
            except:
                save = open(f"save{c}.txt", "x")
                for i in range(len(game)):
                    save.write(f"{self.history[i]}\n")
                save.close()
                break
        

    def loadGame(self, save, board_state):
        save_file = open(save, "r") 
        save_boards = save_file.readlines()
        self.FENstr = save_boards[board_state - 1]
        save_file.close()
        self.playGame()

    def switchBoard(self, board):
        self.FENstr = self.history[board - 1]
        self.playGame()

    def FENToBoard(self):
        game_board = []
        for i in range(len(self.FENstr) - 13):
            match self.FENstr[i]:
                case "/":
                    continue
                case "p":
                    game_board.append(Pawn(i, Chess.PAWN, Chess.WHITE))
                case "P":
                    game_board.append(Pawn(i, Chess.PAWN, Chess.BLACK))
                case "r":
                    game_board.append(Rook(i, Chess.ROOK, Chess.WHITE))
                case "R":
                    game_board.append(Rook(i, Chess.ROOK, Chess.BLACK))
                case "b":
                    game_board.append(Bishop(i, Chess.BISHOP, Chess.WHITE))
                case "B":
                    game_board.append(Bishop(i, Chess.BISHOP, Chess.BLACK))
                case "h":
                    game_board.append(Horse(i, Chess.HORSE, Chess.WHITE))
                case "H":
                    game_board.append(Horse(i, Chess.HORSE, Chess.BLACK))
                case "q":
                    game_board.append(Queen(i, Chess.QUEEN, Chess.WHITE))
                case "Q":
                    game_board.append(Queen(i, Chess.QUEEN, Chess.BLACK))
                case "k":
                    game_board.append(King(i, Chess.KING, Chess.WHITE))
                case "K":
                    game_board.append(King(i, Chess.KING, Chess.BLACK))
                case _:
                    if self.FENstr[i].isnumeric():
                        for j in range(int(self.FENstr[i])):
                            game_board.append(None)
        return game_board
        
        
    def boardToFEN(self):
        FEN = ""
        counter = 0
        blank_count = 0
        for i in range(len(self.board)):
            if counter == 8:
                FEN += "/"
                counter = 0
                blank_count = 0
            match self.board[i]:
                case None:
                    blank_count + 1
                    if self.board[i + 1] != None:
                        FEN += str(blank_count)
                case Pawn():
                    if self.board[i].color == Chess.WHITE:
                        FEN += "p"
                    else:
                        FEN += "P"
                case Rook():
                    if self.board[i].color == Chess.WHITE:
                        FEN += "r"
                    else:
                        FEN += "R"
                case Bishop():
                    if self.board[i].color == Chess.WHITE:
                        FEN += "b"
                    else:
                        FEN += "B"
                case Horse():
                    if self.board[i].color == Chess.WHITE:
                        FEN += "h"
                    else:
                        FEN += "H"
                case Queen():
                    if self.board[i].color == Chess.WHITE:
                        FEN += "q"
                    else:
                        FEN += "Q"
                case King():
                    if self.board[i].color == Chess.WHITE:
                        FEN += "k"
                    else:
                        FEN += "K"
            counter + 1

        if self.turn == True:
            FEN += " w "
        else:
            FEN += " b "
        
        for i in self.board:
            if type(i) == King():
                if i.color == Chess.BLACK:
                    FEN += "K"
                else:
                    FEN += "k"
            if type(i) == Queen():
                if i.color == Chess.BLACK:
                    FEN += "Q"
                else:
                    FEN += "q"
        FEN += f" - {self.movesMade[0]} {self.movesMade[1]}"

        self.history.append(FEN)


    def printBoard(self):
        game = "  a b c d e f g \n"
        for y in range(Chess.BOARD_WIDTH.value):
            game += f"{y + 1} "
            for x in range(Chess.BOARD_WIDTH.value):
                if x == 7:
                    if self.board[x + y * Chess.BOARD_WIDTH.value] == None:
                        game += " \n"
                    else:
                        game += f"{self.board[x + y * Chess.BOARD_WIDTH.value]}\n"
                else:
                    if self.board[x + y * Chess.BOARD_WIDTH.value] == None:
                        game += " |"
                    else:
                        game += f"{self.board[x + y * Chess.BOARD_WIDTH.value]}" + "|"
        print(game)

    def playGame(self):
        decision = input()
        if decision == "load":
            print("Please enter game location:")
            loaded_save = input()
            if loaded_save == "quit":
                self.playGame()
            if ":" not in loaded_save:
                print("Illegal location! Please try again.")
                self.playGame()
            else:
                print("Loading game:")
                self.loadGame(loaded_save)
        if decision == "quit":
            print("Save game? y/n")
            save_or_not = input()
            if save_or_not == "y":
                print("Saving game.")
                self.saveGame()
            if save_or_not == "n":
                print("Quitting.")
            return None
        if decision == "play":
            print("Starting a new game.")
            while True:
                if "k" not in self.FENstr:
                    print("White king is dead! long live the black king!")
                    break
                if "k" not in self.FENstr:
                    print("White king is dead! long live the black king!")
                    break
                self.printBoard()
                move = input()
                if move == "quit":
                    break
                if re.fullmatch("^[a-h][1-8][a-h][1-8]", move):
                    up_start_index = (Chess.LEGAL_CHARS.value.find(move[0]), int(move[1]))
                    up_end_index = (Chess.LEGAL_CHARS.value.find(move[2]), int(move[3]))
                    self.board[up_start_index[0] + up_start_index[1]].move(up_end_index)
                    continue
                else:
                    print("Illegal input! Try agin!")
                    continue
            self.playGame()
        else:
            print("Unknown command! Please try again.")
            self.playGame()
             

def outOfBounds(index: list):
    if index[0] < 0 or index[0] > 7\
    or index[1] < 0 or index[1] > 7:
        return False
    else:
        return True

game = Game()
game.printBoard()
#game.playGame()
