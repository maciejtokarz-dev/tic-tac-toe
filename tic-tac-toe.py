class Board:
    
    def __init__(self):
        self.listOfSquares = ["/  "] * 9
    
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

        if self.listOfSquares[square] == "/  ":
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
        self.turn = player1
        
    def changeTurn(self):
        if self.turn == self.player1:
            self.turn = self.player2
        elif self.turn == self.player2:
                self.turn = self.player1

    def win(self):
        cells = self.board.listOfSquares

        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7 ,8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (3, 4, 6)               
        ]

        for a, b, c in win_conditions:
            if cells[a] == cells[b] == cells[c] and cells[a] != "/  ":
                return True
        return False
    
    def play(self):
        while not self.win():
            self.board.showBoard()

            print(f"Ruch gracza {self.turn.name}")

            if self.turn.move(self.board) == True:
                if self.win():
                    self.board.showBoard()
                    print(f"Player {self.turn.name} won")
                if self.board.draw():
                    self.board.showBoard()
                    print(f"It's draw")
                self.changeTurn()
        self.board.showBoard()
        print("Koniec gry!")




b1 = Board()

#for i in range(9):
#    g1.fillSquare(i, 'X')
p1 = Player("Maciek", "X")
p2 = Player("Zuzia", "Y")
g1 = Game(b1, p1, p2, p1)
g1.play()




