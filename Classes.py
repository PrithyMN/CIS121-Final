import math
class TicTacToe:
  '''
  Makes a 3 by 3 board on which the game will be played on
  A space with value 0 is unclaimed, marked with 1 is for player 1, and 2 for player 2
  '''
  def __init__(self):
    self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #creates 3 by 3 empty board
  
  def clearBoard(self):
    self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  def addValue(self, xPos: int, yPos: int, playerNum):
    if self.board[xPos][yPos] != 0: #checks if the square has already been claimed
      print("Square has already been claimed, try again!")
    else:
      self.board[xPos][yPos] = playerNum #square is claimed by player

  #functions is to make checking for wins easy
  def __checkValuesForWin(self, val1: int, val2: int, val3: int): #double underscore before the name to make it hard to call this function outside of this class defintion
    return val1 == val2 == val3 and val1 != 0
  
  def checkForWin(self):
    #checks for wins along rows
    for curRow in self.board: #iterates through each row
      if self.checkValuesForWin(curRow[0], curRow[1], curRow[2]): #checks if all values in the row are the same
        return curRow[0] #returns the number of the player who has won the game
    
    #checks for wins along columns
    for curCol in range(3): #iterates through each column
      if self.checkValuesForWin(self.board[0][curCol], self.board[1][curCol], self.board[2][curCol]):
        return self.board[0][curCol] #returns the number of the player who has won the game
      
    #checks for wins along diagonals
    if self.checkValuesForWin(self.board[0][0], self.board[1][1], self.board[2][2]): #diagonal 1
      return self.board[0][0] #returns the number of the player who has won the game
    if self.checkValuesForWin(self.board[0][2], self.board[1][1], self.board[2][0]): #diagonal 2
      return self.board[0][2] #returns the number of the player who has won the game
    
  def printBoard(self):
        symbols = {0: '.', 1: 'X', 2: 'O'} #creates dictionary to convert board values to prinable icons (0, 1, 2 -> ., X, O)
        print("\nCurrent board:")
        for row in self.board:
            print(" ".join(symbols[cell] for cell in row))
        print('') #skips line
    
'''
    def playGame(self):
        game = TicTacToe()
        currentPlayer = 1

        while True:
            game.printBoard()
            print(f"Player {currentPlayer}'s turn (X if 1, O if 2).")

            try: #try statement for proper and improper inputs. Loops until a valid input is entered.
                xPos = int(input("Enter row (0-2): "))
                yPos = int(input("Enter column (0-2): "))
                if xPos < 0 or xPos > 2 or yPos < 0 or yPos > 2:
                    print("Invalid input! Row and column must be between 0 and 2.") #detects if input is out of range and tells player
                    continue
            except ValueError:
                print("Invalid input! Please enter integers.")
                continue

            if not game.addValue(xPos, yPos, currentPlayer): #adds the player input to the board. if the square already has a value, the player is told to retry
                print("Square has already been claimed, try again!")
                continue #(Data Collection Type #3 Tuple^)

            winner = game.checkForWin()
            if winner == 1 or winner == 2:
                game.printBoard()
                print(f"Player {winner} wins!") #identifies higher value to assign winner and returns result
                break
            elif game.isFull():
                game.printBoard() #calling printBorard function to show the game board
                print("It's a tie!")
                break

            currentPlayer += 1
            if currentPlayer >= 3: #eliminates possible weirdness if value is over 3 (but gives player 1 an advantage :) ?
                currentPlayer = 1
    '''

