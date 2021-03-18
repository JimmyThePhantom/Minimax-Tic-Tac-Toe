class Game:
    def __init__(self):
        self.board = [" " for _ in range(9)] # The game board. It is represented with a list

        self.playersTurn = True # If true, it's the players turn. If false, its the computer's turn
        self.endGame = False # If true, the game ends

        self.printBoard()
    
    # Checks every possible different win combination, If any of these are true, it return true and the letter that won
    def winCheck(self, board):
        if (board[0] == board[1] and board[0] == board[2] and board[0] != ' '):
            return True, board[0]
        elif (board[3] == board[4] and board[3] == board[5] and board[3] != ' '):
            return True, board[3]
        elif (board[6] == board[7] and board[6] == board[8] and board[6] != ' '):
            return True, board[6]
        elif (board[0] == board[3] and board[0] == board[6] and board[0] != ' '):
            return True, board[0]
        elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
            return True, board[1]
        elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
            return True, board[2]
        elif (board[0] == board[4] and board[0] == board[8] and board[0] != ' '):
            return True, board[0]
        elif (board[6] == board[4] and board[6] == board[2] and board[6] != ' '):
            return True, board[6]
        else:
            return False, False
        
    # Checks for draw
    def checkDraw(self, board):
        for i in range(0, len(board)):
            if (board[i] == ' '):
                return False
        return True

    # Makes the move of the player
    def playerMove(self):
        # Asks for input and checks if it is valud
        move = int(input("Insert your move player. Choose between 1-9: "))

        try:
            temp = self.board[move - 1]
        except:
            print("Position not in board. Try again. ", end="")
            self.playerMove()
            return 0

        while self.board[move - 1] != " ":
            move = int(input("Invalid position. Try again: "))

        self.board[move - 1] = "X"

        # Checks if anyone won to end the game
        if self.winCheck(self.board)[0]:
            self.printBoard()
            print("The player won!")
            self.endGame = True
            return 0
                
        elif self.checkDraw(self.board):
            self.printBoard()
            print("It's a tie!")
            self.endGame = True
            return 0
                
        self.printBoard()
        self.playersTurn = False

    # Makes the move of the computer
    def computerMove(self):
        # Finds the best move
        bestScore = float("-inf")
        bestMove = 0
        for key in range(0, len(self.board)):
            if (self.board[key] == ' '):
                self.board[key] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = key

        self.board[bestMove] = "O"

        # Checks if anyone won to end the game
        if self.winCheck(self.board)[0]:
            self.printBoard()
            print("The computer won!")
            self.endGame = True
            return 0
                
        elif self.checkDraw(self.board):
            self.printBoard()
            print("It's a tie!")
            self.endGame = True
            return 0
                        
        self.printBoard()
        self.playersTurn = True

    # The algorithm responsible for making the best possible move for the computer
    def minimax(self, board, depth, isMaximizing):
        if self.winCheck(board)[1] == "O":
            return 1
        elif self.winCheck(board)[1] == "X":
            return -1
        elif self.checkDraw(board):
            return 0

        # Maximizing player
        if isMaximizing:
            bestScore = float("-inf")
            for key in range(0, len(board)):
                if (board[key] == ' '):
                    board[key] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[key] = ' '
                    if (score > bestScore):
                        bestScore = score
            return bestScore

        # Minimizing player
        else:
            bestScore = float("inf")
            for key in range(0, len(board)):
                if (board[key] == ' '):
                    board[key] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[key] = ' '
                    if (score < bestScore):
                        bestScore = score
            return bestScore

    # Determines whose turn it is and playes it
    def makeTurn(self):
        if self.playersTurn:
            self.playerMove()
        else:
           self.computerMove()
            
    # Prints the board in a nice way
    def printBoard(self):
        print("\n")
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
        print('-+-+-')
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print('-+-+-')
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
        print("\n")
        
    