import random

class Minesweeper:
    
        # Constructor
    def __init__(self, height, length, numbombs):
        # Creates a player board, a bomb board, and places the bombs
        self._height = height
        self._length = length
        self._numbombs = numbombs
        self._turnCount = 0
        self._bombboard = [[0] * self._height for x in range(self._length)]
        self._playerboard = [["-"] * self._height for x in range(self._length)]
        self._placedbombs = 0
        self._win = False
        
        # Creates boards and places bombs randomly
        for x in range(numbombs):
            while self._placedbombs != numbombs:
                self._placedbombs = 0
                self._bombboard[random.randint(0,self._length-1)][random.randint(0,self._height-1)] = -1
                for y in range(self._height):
                    for x in range(self._length):
                        if self._bombboard[x][y] == -1:
                            self._placedbombs += 1
                            
        # Denotes each space on the bomb board with the number of bombs next to the space
        for y in range(self._height):
            for x in range(self._length):
                if self._bombboard[x][y] != -1:
                    self._bombboard[x][y] = self.bombChecker(x, y)
        # Prints out empty board
        self.print()
        
    
    # Prints out the player board with appropriate spacing and with correctly revealed spaces
    def print(self):
        print("  ", end="")
        for i in range(1, len(str(self._height))):
            print(" ", end="")
        for x in range(self._length):
            print(str(x + 1) + " ", end="")
            for i in range(len(str(x + 1)), len(str(self._length))):
                print(" ", end="")
        print()
        for y in range(self._height):
            print(str(y + 1) + " ", end="")
            for i in range(len(str(y+1)), len(str(self._height))):
                print(" ", end="")
            for x in range(self._length):
                if x != self._length - 1:
                    print(str(self._playerboard[x][y]) + " ", end="")
                    for i in range(1, len(str(self._length))):
                        print(" ", end="")
                else:
                    print(str(self._playerboard[x][y]))
                    
    
    # Checks to see if a space has been revealed and is on the board
    # Handles errors with "Invalid Input"
    def checkValid(self, x, y):
        try:
            if self._playerboard[x][y] == "-":
                return True
            else:
                print("Invalid Input")
                return False
        except Exception:
            print("Invalid Input")
            return False
        
        
    # Reveals a space on the player board
    def select(self, x, y, z=1):
        if self.checkValid(x, y):
            if self._bombboard[x][y] == -1:
                self._playerboard[x][y] = "B"
                self.print()
                print("Bomb! You lose.")
                for y in range(self._height):
                    for x in range(self._length):
                        if self._bombboard[x][y] == -1:
                            self._playerboard[x][y] = "B"
            else:
                self._playerboard[x][y] = self._bombboard[x][y]
                self._turnCount += 1
                if self._playerboard[x][y] == 0:
                    self.revealAdj(x,y)
                    
                    
    # Checks if bomb is in the given space and if it is it moves it and then calls select on that space
    def selectFirst(self, x, y):
        if self.checkValid(x,y):
            # Moves bomb if in the selected space
            if self._bombboard[x][y] == -1:
                unplaced = True
                while unplaced:
                    i = random.randint(0,self._length-1)
                    j = random.randint(0,self._height-1)
                    if self._bombboard[i][j] != -1:
                        self._bombboard[i][j] = -1
                        self._bombboard[x][y] = self.bombChecker(x,y)
                        unplaced = False
                        
                # Recreates the bomb board with the newly placed bomb
                for m in range(self._height):
                    for n in range(self._length):
                        if self._bombboard[n][m] != -1:
                            self._bombboard[n][m] = self.bombChecker(n, m)
                self.select(x,y)
            else:
                self.select(x,y)
                
                
    # Flags a space on the player board with an "F"
    def flag(self, x, y):
        if self.checkValid(x,y):
            if self._playerboard[x][y] == "-":
                self._playerboard[x][y] = "F"
            else:
                print("Invalid Input")
                
                
    # Unflags a space on the player board if it has an "F"
    # Handles errors with try, except
    def unflag(self, x, y):
        try:
            if self._playerboard[x][y] == "F":
                self._playerboard[x][y] = "-"
            else:
                print("Invalid Input")
        except Exception:
            print("Invalid Input")
            
            
    # Checks if the game has been won or lost yet
    def checkStatus(self):
        progress = 0
        # Counts the number of spaces revealed so far
        # Checks if any bombs have been revealed
        for y in range(self._height):
            for x in range(self._length):
                if self._playerboard[x][y] == "B":
                    return False
                if str(self._playerboard[x][y]).isdigit():
                    progress += 1
                    
        # Checks if the spaces revealed is the total number of non-bomb spaces
        if progress == self._length * self._height - self._numbombs:
            print("You win!")
            self._win = True
            return False
        
        # If not then the game goes on
        else:
            return True
        
        
    # Reveals all the adjacent spaces on the player board and calls itself again if any of those are a zero
    def revealAdj(self, x, y):
        xstart = 0
        xend = 3
        ystart = 0
        yend = 3
        if x == 0:
            xstart = 1
        if x == self._length-1:
            xend = 2
        if y == 0:
            ystart = 1
        if y == self._height-1:
            yend = 2
        for j in range(ystart,yend):
            for i in range(xstart,xend):
                if self._playerboard[x+i-1][y+j-1] == "-":
                    self.select(x+i-1,y+j-1)
                    
                    
    # Checks to see how many bombs are next to a space and returns it
    def bombChecker(self, x, y):
        bombs = 0
        xstart = 0
        xend = 3
        ystart = 0
        yend = 3
        if x == 0:
            xstart = 1
        if x == self._length - 1:
            xend = 2
        if y == 0:
            ystart = 1
        if y == self._height - 1:
            yend = 2
        for j in range(ystart,yend):
            for i in range(xstart,xend):
                if self._bombboard[x+i-1][y+j-1] == -1:
                    bombs += 1
        return bombs
    
    
    # Asks the player for input and executes the appropriate commands
    def turn(self):
        while self.checkStatus():
            type = ""
            if self._turnCount != 0:
                type = input("“select” or “flag” or “unflag”? ")
                
            x = input("Select an x coordinate: ")
            # Checks to make sure 'x' is valid
            while not x.isdigit() or int(x) <= 0 or int(x) > self._length:
                print("Invalid Input")
                x = input("Select an x coordinate: ")
                
            y = input("Select a y coordinate: ")
            # Checks to make sure 'y' is valid
            while not y.isdigit() or int(y) <= 0 or int(y) > self._height:
                print("Invalid Input")
                y = input("Select a y coordinate: ")
                
            # Converts x and y into integers
            x = int(x)
            y = int(y)
            
            # Calls the appropriate method
            # If the user input for what action to take doesn't match "flag" or "unflag", select is called
            if type == "unflag":
                self.unflag(x - 1, y - 1)
            elif self.checkValid(x-1,y-1):
                if self._turnCount == 0:
                    self.selectFirst(x-1,y-1)
                elif type == "select":
                    self.select(x-1,y-1)
                elif type == "flag":
                    self.flag(x-1,y-1)
                else:
                    print("Invalid Input")
            self.print()
            
            
    # Returns true if the player won the game and false if they lost
    def getWin(self):
        return self._win
    
    
    # Returns the board with all of the spaces revealed
    # Bombs marked as 'B'
    def _getSolution(self):
        for y in range(self._height):
            for x in range(self._length):
                if self._bombboard[x][y] == -1:
                    self._bombboard[x][y] = "B"
        return self._bombboard
