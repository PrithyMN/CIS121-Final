import math

class TicTacToe:
    def __init__(self):
        # Initialize 3x3 board with zeros (0 = unclaimed, 1 = player 1, 2 = player 2)
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def clearBoard(self):
        # Reset the board to all zeros
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def addValue(self, x, y, player):
        # Add a player's mark to the board if space is unclaimed
        if self.board[x][y] == 0:
            self.board[x][y] = player
            return True
        return False

    def __checkValuesForWin(self, a, b, c):
        # Check if all values are the same and not 0 (win condition)
        return a == b == c != 0

    def checkForWin(self):
        # Check rows and columns
        for i in range(3):
            if self.__checkValuesForWin(*self.board[i]):
                return self.board[i][0]
            if self.__checkValuesForWin(self.board[0][i], self.board[1][i], self.board[2][i]):
                return self.board[0][i]

        # Check diagonals
        if self.__checkValuesForWin(self.board[0][0], self.board[1][1], self.board[2][2]):
            return self.board[0][0]
        if self.__checkValuesForWin(self.board[0][2], self.board[1][1], self.board[2][0]):
            return self.board[0][2]

        return 0  # No winner

    def isFull(self):
        # Return True if no empty cells are left
        return all(cell != 0 for row in self.board for cell in row)

    def printBoard(self):
        # Print the board using symbols
        symbols = {0: '.', 1: 'X', 2: 'O'}
        print("\nCurrent board:")
        for row in self.board:
            print(" ".join(symbols[cell] for cell in row))
        print()

    def returnBoard(self):
        return self.board


class GameMode:

    def playGameOntoFile(self, filename="TicTacToe.txt"):
        game = TicTacToe()
        currentPlayer = 1

        # Create or overwrite the log file
        with open(filename, "w") as log:
            log.write("Tic Tac Toe Game Log\n====================\n")

        while True:
            game.printBoard()
            print(f"Player {currentPlayer}'s turn (X if 1, O if 2).")

            # Get user input
            try:
                x = int(input("Enter row (0-2): "))
                y = int(input("Enter column (0-2): "))
                if not (0 <= x <= 2 and 0 <= y <= 2):
                    print("Invalid input! Row and column must be between 0 and 2.")
                    continue
            except ValueError:
                print("Invalid input! Please enter integers.")
                continue

            # Attempt to make the move
            if not game.addValue(x, y, currentPlayer):
                print("Square already claimed. Try again.")
                continue

            # Log the move
            with open(filename, "a") as log:
                log.write(f"Player {currentPlayer} moved to ({x}, {y})\n")
                for row in game.returnBoard():
                    log.write(" ".join(str(cell) for cell in row) + "\n")
                log.write("\n")

            # Check for win or tie
            winner = game.checkForWin()
            if winner:
                game.printBoard()
                print(f"Player {winner} wins!")
                with open(filename, "a") as log:
                    log.write(f"Player {winner} wins!\n")
                break
            elif game.isFull():
                game.printBoard()
                print("It's a tie!")
                with open(filename, "a") as log:
                    log.write("It's a tie!\n")
                break

            # Switch player
            currentPlayer = 2 if currentPlayer == 1 else 1

    def playGames(self, numGames: int):
        pass

    def playUntilWin(self):
        pass


if __name__ == "__main__":
    game = GameMode()
    game.playGameOntoFile("TicTacToe.txt")
