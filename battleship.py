from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)
print #linebreak

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row #temporary, for debugging
print ship_col #temporary, for debugging

for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))-1 #-1 for position to index translation
  guess_col = int(raw_input("Guess Col: "))-1

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"   
    break
  else:
    if guess_row not in range(5) or \
    guess_col not in range(5):
      if (turn == 3):
        print "Oops, that's not even in the ocean."
        print "Game Over"
      else:
        print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      if (turn == 3):
        print "You guessed that one already."
        print "Game Over"
      else:
        print"You guessed that one already."
    else:
      if (turn == 3):
        print "You missed my battleship!"
        print "Game Over"
      else:    
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    print_board(board)
    print 
