import re
import enum
from copy import deepcopy
import os
 
def clear():
    os.system('cls')
 
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
    
    
class Piece():
    def __init__(self, index = None, piece_type = None, color = None):
        self.index = index
        self.y = int(self.index / Chess.BOARD_WIDTH.value)
        self.x = self.index % Chess.BOARD_WIDTH.value
        self.piece_type = piece_type
        self.color = color
        self.direction = None
        self.has_moved = False
        self.possible_moves = []
 
        if self.piece_type == Chess.PAWN:
            if self.color.value == True:
                self.direction = -1
            else:
                self.direction = 1
 
 
    def __repr__(self) -> str:
        str = self.piece_type.value
        if self.color == Chess.BLACK:
            str = str.upper() 
        return str
 
 
    def move(self, up_end_index):
        self.possible_moves = []
        match self.piece_type:
            case Chess.PAWN:
                self.pawn_move()
                self.move_finalize(up_end_index)
            case Chess.ROOK:
                self.rook_move()
                self.move_finalize(up_end_index)
            case Chess.BISHOP:
                self.bishop_move()
                self.move_finalize(up_end_index)
            case Chess.HORSE:
                self.horse_move()
                self.move_finalize(up_end_index)
            case Chess.QUEEN:
                self.rook_move()
                self.bishop_move()
                self.move_finalize(up_end_index)
            case Chess.KING:
                self.king_move()
                self.move_finalize(up_end_index)
 
 
    def pawn_move(self):
        if self.has_moved == False\
            and game.board[self.y * Chess.BOARD_WIDTH.value + 2 * self.direction * Chess.BOARD_WIDTH.value + self.x] == None:
            self.possible_moves.append((self.y + 2 * self.direction, self.x))
        
        if game.board[self.y * Chess.BOARD_WIDTH.value + 1 * self.direction * Chess.BOARD_WIDTH.value + self.x] == None\
            and outOfBounds(self.y + 1 * self.direction, self.x):
            self.possible_moves.append((self.y + 1 * self.direction, self.x))
        
        if game.board[self.y * Chess.BOARD_WIDTH.value + 1 * self.direction * Chess.BOARD_WIDTH.value + self.x - 1] != None\
            and game.board[self.y * Chess.BOARD_WIDTH.value + 1 * self.direction * Chess.BOARD_WIDTH.value + self.x - 1].color.value != self.color.value\
            and outOfBounds(self.y + 1 * self.direction, self.x - 1):
            self.possible_moves.append((self.y + 1 * self.direction, self.x - 1))
 
        if game.board[self.y * Chess.BOARD_WIDTH.value + 1 * self.direction * Chess.BOARD_WIDTH.value + self.x + 1] != None\
            and game.board[self.y * Chess.BOARD_WIDTH.value + 1 * self.direction * Chess.BOARD_WIDTH.value + self.x + 1].color.value != self.color.value\
            and outOfBounds(self.y + 1 * self.direction, self.x + 1):
            self.possible_moves.append((self.y + 1 * self.direction, self.x + 1))
 
 
    def rook_move(self):
        if self.has_moved == False:
            match self.index:
                case 0:
                    self.possible_moves.append((0,2))
                case 7:
                    self.possible_moves.append((0,5))
                case 56:
                    self.possible_moves.append((7,2))
                case 63:
                    self.possible_moves.append((7,5))
 
        free_l = True
        free_r = True
        free_u = True
        free_d = True
        i = 1
        while free_l or free_r or free_u or free_d:
            if outOfBounds(self.y, self.x - i) and free_l:
                if game.board[self.index - i] == None:
                    self.possible_moves.append((self.y, self.x - i))
                else:
                    if game.board[self.index - i].color.value != self.color.value:
                        self.possible_moves.append((self.y, self.x - i))
                        free_l = False
                    else:
                        free_l = False
            else:
                free_l = False
 
            if outOfBounds(self.y, self.x + i) and free_r:
                if game.board[self.index + i] == None:
                    self.possible_moves.append((self.y, self.x + i))
                else:
                    if game.board[self.index + i].color.value != self.color.value:
                        self.possible_moves.append((self.y, self.x + i))
                        free_r = False
                    else:
                        free_r = False
            else:
                free_r = False
 
            if outOfBounds(self.y - i, self.x) and free_u:
                if game.board[self.index - i * Chess.BOARD_WIDTH.value] == None:
                    self.possible_moves.append((self.y - i, self.x))
                else:
                    if game.board[self.index - i * Chess.BOARD_WIDTH.value].color.value != self.color.value:
                        self.possible_moves.append((self.y - i, self.x))
                        free_u = False
                    else:
                        free_u = False
            else:
                free_u = False
 
            if outOfBounds(self.y + i, self.x) and free_d:
                if game.board[self.index + i * Chess.BOARD_WIDTH.value] == None:
                    self.possible_moves.append((self.y + i, self.x))
                else:
                    if game.board[self.index + i * Chess.BOARD_WIDTH.value].color.value != self.color.value:
                        self.possible_moves.append((self.y + i, self.x))
                        free_d = False
                    else:
                        free_d = False
            else:
                free_d = False
 
            i += 1
 
 
    def bishop_move(self):
        free_lu = True
        free_ru = True
        free_ld = True
        free_rd = True
        i = 1
        while free_lu or free_ru or free_ld or free_rd:
            if outOfBounds(self.y - i, self.x - i) and free_lu :
                if game.board[self.index - i - i * Chess.BOARD_WIDTH.value] == None:
                    self.possible_moves.append((self.y - i, self.x - i))
                else:
                    if game.board[self.index - i - i * Chess.BOARD_WIDTH.value].color.value != self.color.value:
                        self.possible_moves.append((self.y - i, self.x - i))
                        free_lu = False
                    else:
                        free_lu = False
            else:
                free_lu = False
 
            if outOfBounds(self.y - i,self.x + i) and free_ru:
                if game.board[self.index + i - i * Chess.BOARD_WIDTH.value] == None:
                    self.possible_moves.append((self.y - i, self.x + i))
                else:
                    if game.board[self.index + i - i * Chess.BOARD_WIDTH.value].color.value != self.color.value:
                        self.possible_moves.append((self.y - i, self.x + i))
                        free_ru = False
                    else:
                        free_ru = False
            else:
                free_ru = False
 
            if outOfBounds(self.y + i, self.x - i) and free_ld:
                if game.board[self.index - i + i * Chess.BOARD_WIDTH.value] == None:
                    self.possible_moves.append((self.y + i, self.x - i))
                else:
                    if game.board[self.index - i + i * Chess.BOARD_WIDTH.value].color.value != self.color.value:
                        self.possible_moves.append((self.y + i, self.x - i))
                        free_ld = False
                    else:
                        free_ld = False
            else:
                free_ld = False
 
            if outOfBounds(self.y + i, self.x + i) and free_rd:
                if game.board[self.index + i + i * Chess.BOARD_WIDTH.value] == None:
                    self.possible_moves.append((self.y + i, self.x + i))
                else:
                    if game.board[self.index + i + i * Chess.BOARD_WIDTH.value].color.value != self.color.value:
                        self.possible_moves.append((self.y + i, self.x + i))
                        free_rd = False
                    else:
                        free_rd = False
            else:
                free_rd = False
 
            i += 1
 
 
    def horse_move(self, up_end_index):
        if outOfBounds(self.y + 1, self.x - 2):
            if game.board[(self.x - 2) + (self.y + 1) * Chess.BOARD_WIDTH.value] == None:
                self.possible_moves.append((self.y + 1, self.x - 2))
            elif game.board[(self.x - 2) + (self.y + 1) * Chess.BOARD_WIDTH.value].color != self.color:
                self.possible_moves.append((self.y + 1, self.x - 2))
        if outOfBounds(self.y + 1 ,self.x + 2):
            if game.board[(self.x + 2) + (self.y + 1) * Chess.BOARD_WIDTH.value] == None:
                self.possible_moves.append((self.y + 1, self.x + 2))
            elif game.board[(self.x + 2) + (self.y + 1) * Chess.BOARD_WIDTH.value].color != self.color:
                self.possible_moves.append((self.y + 1, self.x + 2))
        if outOfBounds(self.y - 1 ,self.x - 2):
            if game.board[(self.x - 2) + (self.y - 1) * Chess.BOARD_WIDTH.value] == None:
                self.possible_moves.append((self.y - 1 ,self.x - 2))
            elif game.board[(self.x - 2) + (self.y - 1) * Chess.BOARD_WIDTH.value].color != self.color:
                self.possible_moves.append((self.y - 1 ,self.x - 2))
        if outOfBounds(self.y - 1, self.x + 2):
            if game.board[(self.x + 2) + (self.y - 1) * Chess.BOARD_WIDTH.value] == None:
                self.possible_moves.append((self.y - 1, self.x + 2))
            elif game.board[(self.x + 2) + (self.y - 1) * Chess.BOARD_WIDTH.value].color != self.color:
                self.possible_moves.append((self.y - 1, self.x + 2))
        if outOfBounds(self.y + 2 ,self.x - 1):
            if game.board[(self.x - 1) + (self.y + 2) * Chess.BOARD_WIDTH.value] == None:
                self.possible_moves.append((self.y + 2, self.x - 1))
            elif game.board[(self.x - 1) + (self.y + 2) * Chess.BOARD_WIDTH.value].color != self.color:
                self.possible_moves.append((self.y + 2, self.x - 1))
        if outOfBounds(self.y + 2, self.x + 1):
            if game.board[(self.x + 1) + (self.y + 2) * Chess.BOARD_WIDTH.value] == None:
                self.possible_moves.append((self.y + 2, self.x + 1))
            elif game.board[(self.x + 1) + (self.y + 2) * Chess.BOARD_WIDTH.value].color != self.color:
                self.possible_moves.append((self.y + 2, self.x + 1))
        if outOfBounds(self.y - 2, self.x - 1):
            if game.board[(self.x - 1) + (self.y - 2) * Chess.BOARD_WIDTH.value] == None:
                self.possible_moves.append((self.y - 2, self.x - 1))
            elif game.board[(self.x - 1) + (self.y - 2) * Chess.BOARD_WIDTH.value].color != self.color:
                self.possible_moves.append((self.y - 2, self.x - 1))
        if outOfBounds(self.y - 2, self.x + 1):
            if game.board[(self.x + 1) + (self.y - 2) * Chess.BOARD_WIDTH.value] == None:
                self.possible_moves.append((self.y - 2, self.x + 1))
            elif game.board[(self.x + 1) + (self.y - 2) * Chess.BOARD_WIDTH.value].color != self.color:
                self.possible_moves.append((self.y - 2, self.x + 1))
 
    
    def king_move(self, up_end_index):
        for y in range(-1,2):
            for x in range(-1,2):
                if x == 0 and y == 0:
                    continue
                if outOfBounds(y + self.y, x + self.x):
                    if game.board[(y + self.y) * Chess.BOARD_WIDTH.value + (x + self.x)] == None:
                        self.possible_moves.append(())
                    elif game.board[(y + self.y) * Chess.BOARD_WIDTH.value + (x + self.x)].color.value != self.color.value:
                        self.possible_moves.append(())
        
        match self.color.value:
            case True:
                if game.board[0] != None\
                    and game.board[0].color.value == self.color.value\
                    and game.board[0].has_moved == False\
                    and game.board[1] == None\
                    and game.board[2] == None\
                    and game.board[3] == None\
                    and self.has_moved == False:
                    self.possible_moves.append((0, 1))
                if game.board[7] != None\
                    and game.board[7].color.value == self.color.value\
                    and game.board[7].has_moved == False\
                    and game.board[5] == None\
                    and game.board[6] == None\
                    and self.has_moved == False:
                    self.possible_moves.append((0, 6))
            case False:
                if game.board[56] != None\
                    and game.board[56].color.value == self.color.value\
                    and game.board[56].has_moved == False\
                    and game.board[57] == None\
                    and game.board[58] == None\
                    and game.board[59] == None\
                    and self.has_moved == False:
                    self.possible_moves.append((7, 1))
                if game.board[63] != None\
                    and game.board[63].color.value == self.color.value\
                    and game.board[63].has_moved == False\
                    and game.board[61] == None\
                    and game.board[62] == None\
                    and self.has_moved == False:
                    self.possible_moves.append((7, 6))
        
        if up_end_index in self.possible_moves and game.turn == self.color.value:
            if up_end_index == (0, 1) and game.board[0] != None and game.board[0].color.value == self.color.value:
                game.board[0].move((0,2))
            if up_end_index == (0, 6) and game.board[7] != None and game.board[7].color.value == self.color.value:
                game.board[0].move((0,5))
            if up_end_index == (7, 1) and game.board[56] != None and game.board[56].color.value == self.color.value:
                game.board[0].move((7,2))
            if up_end_index == (7, 1) and game.board[56] != None and game.board[56].color.value == self.color.value:
                game.board[0].move((7,5))
 
 
    def move_finalize(self, up_end_index):
        if up_end_index in self.possible_moves and game.turn == self.color.value:
            old_index = deepcopy(self.index)
            self.index = up_end_index[0] * Chess.BOARD_WIDTH.value + up_end_index[1]
            self.x = up_end_index[1]
            self.y = up_end_index[0]
            game.board[up_end_index[0] * Chess.BOARD_WIDTH.value + up_end_index[1]] = deepcopy(self)
            game.board[old_index] = None
            self.has_moved = True
 
            if self.color.value == False:
                game.movesMade[0] + 1
            else:
                game.movesMade[1] + 1
 
            game.turn = not game.turn
 
            game.boardToFEN()
 
            return True
 
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
                for i in range(len(self.history)):
                    save.write(f"{self.history[i]}\n")
                save.close()
                break
        
 
    def loadGame(self, save = None, board_state = 1):
        while True:
                print("Please enter game location:")
                loaded_save = input()
                if loaded_save == "quit":
                    return
                if ":" not in loaded_save:
                    print("Illegal location! Please try again.")
                    continue
                else:
                    print("Loading game:")
                    with open(loaded_save, "r") as save_file:
                        save_boards = save_file.readlines()
                        self.FENstr = save_boards[board_state - 1]
                        return
 
 
    def switchBoard(self, board):
        self.FENstr = self.history[board - 1]
        self.startGame()
 
 
    def FENToBoard(self):
        game_board = []
        FEN = ""
        for i in range(len(self.FENstr)):
            if self.FENstr[i] == " ":
                break
            else:
                FEN += self.FENstr[i]
        counter = 0
        for i in range(len(FEN)):
            match self.FENstr[i]:
                case "p":
                    game_board.append(Piece(counter, Chess.PAWN, Chess.WHITE))
                case "P":
                    game_board.append(Piece(counter, Chess.PAWN, Chess.BLACK))
                case "r":
                    game_board.append(Piece(counter, Chess.ROOK, Chess.WHITE))
                case "R":
                    game_board.append(Piece(counter, Chess.ROOK, Chess.BLACK))
                case "b":
                    game_board.append(Piece(counter, Chess.BISHOP, Chess.WHITE))
                case "B":
                    game_board.append(Piece(counter, Chess.BISHOP, Chess.BLACK))
                case "h":
                    game_board.append(Piece(counter, Chess.HORSE, Chess.WHITE))
                case "H":
                    game_board.append(Piece(counter, Chess.HORSE, Chess.BLACK))
                case "q":
                    game_board.append(Piece(counter, Chess.QUEEN, Chess.WHITE))
                case "Q":
                    game_board.append(Piece(counter, Chess.QUEEN, Chess.BLACK))
                case "k":
                    game_board.append(Piece(counter, Chess.KING, Chess.WHITE))
                case "K":
                    game_board.append(Piece(counter, Chess.KING, Chess.BLACK))
                case _:
                    if self.FENstr[i].isnumeric():
                        for j in range(int(self.FENstr[i])):
                            game_board.append(None)
                            counter += 1
                    counter -= 1
            counter += 1
        return game_board
        
        
    def boardToFEN(self):
        FEN = ""
        counter = 0
        blank_count = 0
        for i in range(63):
            if counter == 8:
                FEN += "/"
                counter = 0
                blank_count = 0
            if self.board[i] != None:
                match self.board[i].piece_type:
                    case None:
                        blank_count + 1
                        if self.board[i + 1] != None:
                            FEN += str(blank_count)
                    case Chess.PAWN:
                        if self.board[i].color == Chess.WHITE:
                            FEN += "p"
                        else:
                            FEN += "P"
                    case Chess.ROOK:
                        if self.board[i].color == Chess.WHITE:
                            FEN += "r"
                        else:
                            FEN += "R"
                    case Chess.BISHOP:
                        if self.board[i].color == Chess.WHITE:
                            FEN += "b"
                        else:
                            FEN += "B"
                    case Chess.HORSE:
                        if self.board[i].color == Chess.WHITE:
                            FEN += "h"
                        else:
                            FEN += "H"
                    case Chess.QUEEN:
                        if self.board[i].color == Chess.WHITE:
                            FEN += "q"
                        else:
                            FEN += "Q"
                    case Chess.KING:
                        if self.board[i].color == Chess.WHITE:
                            FEN += "k"
                        else:
                            FEN += "K"
                counter += 1
 
        if self.turn == True:
            FEN += " w "
        else:
            FEN += " b "
 
        for i in self.board:
            if type(i) == type(Piece) and i.piece_type == Chess.KING:
                if i.color == Chess.BLACK:
                    FEN += "K"
                else:
                    FEN += "k"
            if type(i) == type(Piece) and i.piece_type == Chess.QUEEN:
                if i.color == Chess.BLACK:
                    FEN += "Q"
                else:
                    FEN += "q"
        FEN += f" - {self.movesMade[0]} {self.movesMade[1]}"
 
        self.history.append(FEN)
        self.FENstr = FEN
 
 
    def printBoard(self):
        game = "  1 2 3 4 5 6 7 8\n"
        for y in range(Chess.BOARD_WIDTH.value):
            game += f"{Chess.LEGAL_CHARS.value[y]} "
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
 
 
    def startGame(self):
        clear()
        decision = input()
        if decision == "load":
            self.loadGame()
 
        if decision == "quit":
            self.quitGame()
 
        if decision == "play":
            print("Starting a new game.")
            while True:
                if "k" not in self.FENstr:
                    print("White king is dead! long live the black king!")
                    break
                if "K" not in self.FENstr:
                    print("Black king is dead! long live the white king!")
                    break
                
                self.printBoard()
 
                if game.turn == True:
                    print("Turn: white")
                else:
                    print("Turn: black")
 
                decision = input()
 
                if decision == "quit":
                   self.quitGame()
 
                if re.fullmatch(r"^[a-h][1-8][a-h][1-8]", decision):
                    up_start_index = (Chess.LEGAL_CHARS.value.find(decision[0]), int(decision[1]) - 1)
                    up_end_index = (Chess.LEGAL_CHARS.value.find(decision[2]), int(decision[3]) - 1)
 
                    if up_end_index != up_start_index\
                        and self.board[up_start_index[0] * Chess.BOARD_WIDTH.value + up_start_index[1]].move(up_end_index):
                        continue
 
                else:
                    print("Illegal input! Try again!")
                    continue
        else:
            print("Unknown command! Please try again.")
            self.startGame()
 
 
    def quitGame(self):
        print("Do you really want to quit?(y/n)")
        decision = input()
        if decision == "y":
            print("Save game? y/n")
            decision = input()
            if decision == "y":
                print("Saving game.")
                self.saveGame()
            if decision == "n":
                print("Quitting.")
                exit()
        if decision == "n":
            print("Returning to menu.")
            self.startGame()
 
 
def outOfBounds(y, x):
    if y < 0 or y > 7\
    or x < 0 or x > 7:
        return False
    else:
        return True
 
game = Game()
game.startGame()