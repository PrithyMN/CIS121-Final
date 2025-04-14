import math
class TicTacToe:
  def __init__(self):
    self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #creates 3 by 3 board
  
  def clearBoard(self):
    self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  def addValue(self, xPos: int, yPos: int, playerNum):
    if self.board[xPos][yPos] != 0: #checks if the square has already been claimed
      print("Square has already been claimed")
    else:
      self.board[xPos][yPos] = playerNum #square is claimed by player

  def checkValuesForWin(self, val1: int, val2: int, val3: int):
    return val1 == val2 == val3 and val1 != 0
  
  def checkForWin(self):

    for curRow in self.board: #iterates through each row
      if self.checkValuesForWin(curRow[0], curRow[1], curRow[2]): #checks if all values in the row are the same
        return curRow[0] #returns the number of the player who has won the game
      
    for curCol in range(3): #iterates through each column
      if self.checkValuesForWin(self.board[0][curCol], self.board[1][curCol], self.board[2][curCol]):
        return self.board[0][curCol] #returns the number of the player who has won the game
      
    if self.checkValuesForWin(self.board[0][0], self.board[1][1], self.board[2][2]): #checks first diagonal
      return self.board[0][0] #returns the number of the player who has won the game
    if self.checkValuesForWin(self.board[0][2], self.board[1][1], self.board[2][0]): #checks second diagonal
      return self.board[0][2] #returns the number of the player who has won the game

