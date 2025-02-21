
from colorama import init
from termcolor import colored


class Node():
  def __init__(self, row, column, player):
    self.coords = {"row":row, "column":column}
    self.player_num = player
    self.horizontal_length = 1
    self.vertical_length = 1
    self.diagonal_R_length = 1
    self.diagonal_L_length = 1

  def is_winner(self):
    return self.horizontal_length >= 4 or self.vertical_length >= 4 \
      or self.diagonal_L_length >= 4 or self.diagonal_R_length >= 4
  
  def vertical_update(self, game_board):
    row_num = self.coords["row"]
    col_num = self.coords["column"]

    if row_num >= 0 and row_num < 5: # If lower neighbor is a Node and is from the same player
      if type(game_board.cells[row_num + 1][col_num]) is Node and game_board.cells[row_num + 1][col_num].player_num == self.player_num:
        self.vertical_length = game_board.cells[row_num + 1][col_num].vertical_length + 1 # This vert_chain length = previous length + 1
    # No need to check for row == 5. If you drop a token and it's on the bottom row, it cannot have a neighbor above it

  def horizontal_update(self, game_board):
    row_num = self.coords["row"]
    col_num = self.coords["column"]

    if col_num > 0 and col_num < 6:  # If dropped in the middle, check for nodes left & right for a friendly node
      right_neighbor_length = 0
      left_neighbor_length = 0

      if type(game_board.cells[row_num][col_num - 1]) is Node and game_board.cells[row_num][col_num - 1].player_num == self.player_num: # Check left
        left_neighbor_length = game_board.cells[row_num][col_num - 1].horizontal_length + 1 # This horz_chain length = previous length + 1
      if type(game_board.cells[row_num][col_num + 1]) is Node and game_board.cells[row_num][col_num + 1].player_num == self.player_num: # Check right
        right_neighbor_length = game_board.cells[row_num][col_num + 1].horizontal_length + 1 # This horz_chain length = previous length + 1
      
      if right_neighbor_length and left_neighbor_length: # If there are chains to the nodes left and right
        self.horizontal_length = left_neighbor_length + right_neighbor_length + 1 # Add this node and add their lengths together 
      else: # Else i'm missing a partner on 1 side or missing on both sides
        self.horizontal_length = max(left_neighbor_length, right_neighbor_length, self.horizontal_length) #Pick the biggest between myself (1) or the other chain

    elif col_num == 0:  # If on the left wall, and right neighbor is a Node and is from the same player
      if type(game_board.cells[row_num][col_num + 1]) is Node and game_board.cells[row_num][col_num + 1].player_num == self.player_num:
        self.horizontal_length = game_board.cells[row_num][col_num + 1].horizontal_length + 1 # This horz_chain length = previous length + 1
    elif col_num == 6:  # If on the right wall, and left neighbor is a Node and is from the same player
      if type(game_board.cells[row_num][col_num - 1]) is Node and game_board.cells[row_num][col_num - 1].player_num == self.player_num:
        self.horizontal_length = game_board.cells[row_num][col_num - 1].horizontal_length + 1 # This horz_chain length = previous length + 1
  
  # new diag sketch
  # Diag_Right:
  #        o     
  #     x      
  #  o       
  #         
  # Diag_Left:              
  #  o         
  #     x        
  #        o      
  #             


  def update_from_neighbors(self, gameboard):
    self.vertical_update(gameboard)
    self.horizontal_update(gameboard)
    self.diag_left_update(gameboard)
    self.diag_right_update(gameboard)
    pass
    
  

# 7 cols 6 rows
class Game_Board():
  def __init__(self):
    self.cells = []
    self.create_board()
    self.game_over = False
  

  def create_board(self):
    rows, columns = (6, 7)
    for _ in range(rows):
      self.cells.append([0]*columns)
  
  def is_game_over(self): # TODO is_game_over(self, node) return node.is_winner()
    return self.game_over
  
  def is_column_full(self, column_number):  # Returns true if all values are truthy (if column values are all != 0)
    return all(row[column_number] for row in self.cells)
  
  def drop_token(self, player_num, column_index):
    column = [row[column_index] for row in self.cells]
    for row_index, cell in enumerate(column):
      if cell == 0: # If the cell is empty
        new_node = Node(row_index, column_index, player_num)  # change to player num
        new_node.update_from_neighbors(self)
        self.cells[row_index][column_index] = new_node
        break
    


def print_board(game_board):
  row = 7
  while row > 0:
    output = "" # Reset row string
    col = 6 # reset column counter
    while col > -1: # Decrement while
      if row == 7:  # First row is display row for player choice
        output += f"|   {col + 1}   "
      elif type(game_board.cells[row-1][col]) is Node:  # If the space is occupied by a Node
        if game_board.cells[row-1][col].player_num == 1:  # Print for player 1
          output += ("|   " + colored("X", 'red') + "   ")
        elif game_board.cells[row-1][col].player_num == 2: # Print for player 2
          output += ("|   " + colored("O", 'green') + "   ")
      else: # If the space is NOT occupied by a Node
        output += f"| ***** "   # Print blank space

      col -= 1  # Decrement column counter
    print(output + "|\n")
    row -= 1



def get_valid_column_from_player(board, player_num):
  # ask the first player for input
    formatted_token_drop_question = None
    if player_num == 1:
      formatted_token_drop_question = f"Player {colored("ONE","red")}, choose where to drop your token: "
    elif player_num == 2:
      formatted_token_drop_question = f"Player {colored("TWO","green")}, choose where to drop your token: "
    else:
      formatted_token_drop_question = f"Player {colored("UNKNOWN","yellow")}, choose where to drop your token: "
    
    column_choice = input(formatted_token_drop_question)

    valid_column = False
    while not valid_column:
      while column_choice not in ['1', '2','3','4','5','6','7']:  # input validation
        print("Invalid column number. Try again")
        column_choice = input(formatted_token_drop_question)

      column_choice = int(column_choice) - 1  # convert to int

      if board.is_column_full(column_choice):  # check that the column has space
        valid_column = False
      else:
        valid_column = True
    
    return column_choice

init()

game_board = Game_Board() # Setup the board
still_playing = True

while still_playing:
  # Start the game
  playing_choice = input("Welcome to Connect 4! Do you want to play? (y/n): ").lower()
  while playing_choice not in ['y', 'n']: # Validate the users input choice
    playing_choice = input("Invalid input. Do you want to play connect 4? (y/n): ").lower()

  if playing_choice == 'n': # If they want to stop playing
    still_playing = False # Then they are not still playing (this is a safety precaution, maybe not needed)
    break   # break out of the while loop
  
  while not game_board.is_game_over():
    player_one = 1
    player_two = 2

    print_board(game_board) # print the board state
    column = get_valid_column_from_player(game_board, player_one)  # ask the first player for input
    game_board.drop_token(player_one, column)


    print_board(game_board) # print the board state
    column = get_valid_column_from_player(game_board, player_two)    # ask the second player for input
    game_board.drop_token(player_two, column)
    

  print_board(game_board)
  continue_playing_choice = input("Winner winner chicken dinner! Would you like to play again? (y/n): ").lower()
  while continue_playing_choice not in ['y', 'n']: # Validate the users input choice
    continue_playing_choice = input("Invalid input. Would you like to play again? (y/n): ").lower()
  if continue_playing_choice == 'n':  # If they want to quit
    still_playing = False # Then they are not still playing
  
print("Program over. Goodnight y'all")