class Player():
    def __init__(self, name, game_piece):
        self.name = name
        self.game_piece = game_piece
        

class Move():
    def __init__(self, player, position):
        self.player = player
        self.position = position

class Board():
    board_state = [[" ","1","2","3"],
                   ["1", "-","-","-"], 
                   ["2", "-","-","-"], 
                   ["3", "-","-","-"]]

    def display(self):
        for line in self.board_state:
            print(" ".join(line))


    def add_move(self, move):
        row = move.position[0]
        column = move.position[1]
        self.board_state[row][column] = move.player.game_piece

class Game():
    def __init__(self, board, p1, p2):
        self.board = board
        self.p1 = p1
        self.p2 = p2

    def check_win(self, board, mark):


        for index in range(1,4):
            #check rowa
            if (board.board_state[1][index] == 
                board.board_state[2][index] ==
                board.board_state[3][index] ==
                mark):
                return True
            #check cols
            elif (board.board_state[index][1] == 
                  board.board_state[index][2] ==
                  board.board_state[index][3] ==
                  mark):
                return True

        #check diagonals
        if (
            (board.board_state[1][1] == 
            board.board_state[2][2] ==
            board.board_state[3][3] ==
            mark) 
            or
            (board.board_state[1][3] == 
            board.board_state[2][2] ==
            board.board_state[3][1] ==
            mark)
            ):
            return True

        return False

    def check_stalemate(self,board):
        for row in board.board_state:
            if "-" in row:
                return False

        return True

#============START GAME===========================

import re

print("Welcome to Tic Tac Toe!")

#first check for valid marker input by player
valid_mark = False

player_1_name = input("What is your name? ")
    
while not valid_mark:
    mark = input("Would you like to be an X or an O? " ).upper()

    #assign player 2 whatever mark player 1 does not pick
    if mark == "X":
        p2_mark = "O"
    elif mark == "O":
        p2_mark = "X"
    else:
        #if a valid mark is not input, ask the player again
        print("X or O, I said. Let's try this again.")

    #exit the loop if the mark is valid
    valid_mark = mark in ["X", "O"]

player_2_name = input("What is your name, player 2? ")

#instantiate game objects
p1 = Player(player_1_name, mark)
p2 = Player(player_2_name, p2_mark)

my_board = Board()

my_game = Game(my_board, p1, p2)

playing = True

player = p1

while playing: 

    my_board.display()
    print("\n") 

    print(f"{player.name}'s turn.")
    pos = input("Pick a spot: row, col: ")

    #using regular expression to check for proper input
    if re.search(r'[1-3],[1-3]', pos) == None:
        print("Buddy. I need you to dig real deep here.")
        print("Put a comma between those bad boys, give me two numbers.")
        print("You can look at the board to see the corresponding numbers.")
        continue

    #parse out row and column from player input
    pos = pos.split(",")
    pos = [int(pos[0]), int(pos[1])]

    player_move = Move(player, pos)

    my_board.add_move(player_move)

    if my_game.check_win(my_board, player.game_piece):
        print(f'{player.name} wins!')
        playing = False
    elif my_game.check_stalemate(my_board):
        print('No one is a winner today :(')
        playing = False


    #swtich to the next player
    if player == p1:
        player = p2
    else:
        player = p1