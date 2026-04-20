class Board:
    
    def __init__(self):
        self.listOfSquares = ["NULL"] * 9
        i = 0
    
    def showBoard(self):
        for i, square in enumerate(self.listOfSquares):

            print(square, end=" ")

            if (i+1) % 3 == 0:
                print()

        return self.listOfSquares

    def fillSquare(self, square, type):
        self.square = square
        self.type = type
        
        if type == 'X':
            if self.listOfSquares[square] == 'NULL':
                self.listOfSquares[square] = 'X'
            else:
                print("Square have to be empty! ")
        elif type == 'O':
            if self.listOfSquares[square] == 'NULL':
                self.listOfSquares[square] = 'O'
            else:
                print("Square have to be empty! ")


    
g1 = Board()
g1.fillSquare(0, 'X')
g1.fillSquare(0, 'X')
g1.showBoard()



