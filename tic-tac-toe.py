class Board:
    
    def __init__(self):
        self.listOfSquares = ["NULL  "] * 9
    
    def showBoard(self):
        print("-----")
        for i, square in enumerate(self.listOfSquares):
            print(square, end="")
            if(i+1) % 3 == 0:
                print()
        print("-----")

    def fillSquare(self, square, symbol):
         
        if not (0 <= square <= 8):
            print(f"Indeks {square} nie poprawny! Wybierz indeks z przedzialu: (0-8)")
            return False

        if self.listOfSquares[square] == "NULL  ":
            self.listOfSquares[square] = symbol + '  '
            return True
        else:
            print(f"Square {square} have to be empty! Choose another square")
            return False

    def draw(self):
        if "NULL" not in self.listOfSquares:
            print(f"It's a draw ladies and gentlemens! Now it's time for a rematch!")
            return True
        return False
    
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def move(self, board):
        try:
            square = int(input("Type a number of square: "))
            return board.fillSquare(square, self.symbol)
        except ValueError:
            print("You have to type a number!")
            return False

class Game:
    def __init__(self, board, player1, player2, turn):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.turn = turn
        
    def changeTurn(self):
        if self.turn == p1:
            self.turn = p2
        elif self.turn == p2:
                self.turn = p1



b1 = Board()

#for i in range(9):
#    g1.fillSquare(i, 'X')
p1 = Player("Maciek", "X")
p2 = Player("Bartosz", "Y")
g1 = Game(b1, p1, p2, p1)
p1.move(b1)
g1.changeTurn()
p2.move(b1)




