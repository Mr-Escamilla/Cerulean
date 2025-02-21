
from colorama import init
from termcolor import colored

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
  
  def is_game_over(self):
    return self.game_over
  
  def is_column_full(self, column_number):  # Returns true if all values are truthy (if column values are all != 0)
    return all(row[column_number] for row in self.cells)
  
  def drop_token(self, player_num, column_index):
    column = [row[column_index] for row in self.cells]
    for row, cell in enumerate(column):
      if cell == 0:
        self.cells[row][column_index] = player_num  # change to player num
        break
    


def print_board(game_board):
  row = 7
  while row > 0:
    output = ""
    col = 6
    while col > -1:
      if row == 7:
        output += f"|   {col + 1}   "
      elif game_board.cells[row-1][col] == 1:
        output += ("|   " + colored("X", 'red') + "   ")
      elif game_board.cells[row-1][col] == 2:
        output += ("|   " + colored("O", 'green') + "   ")
      else:
        output += f"| ***** "

      col -= 1
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