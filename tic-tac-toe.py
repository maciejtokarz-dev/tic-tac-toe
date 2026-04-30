class Board:
    
    def __init__(self):
        self.listOfSquares = ["NULL"] * 9
    
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
            return

        if self.listOfSquares[square] == "NULL":
            self.listOfSquares[square] = symbol
        else:
            print(f"Square {square} have to be empty! Choose another square")

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
            board.fillSquare(square, self.symbol)
            board.showBoard()
        except ValueError:
            print("You have to type a number!")

g1 = Board()

#for i in range(9):
#    g1.fillSquare(i, 'X')
p1 = Player("Maciek", "X")
p1.move(g1)

g1.showBoard()



