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

    def move(self):
        square = input("Type a number of empty square: ")
        self.fillSquare(square, self.symbol)
        self.showBoard()

g1 = Board()

#for i in range(9):
#    g1.fillSquare(i, 'X')
p1 = Player("maciek", "X")
p1.move()

g1.showBoard()
g1.draw()



