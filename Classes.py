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

