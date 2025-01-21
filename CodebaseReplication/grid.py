# import sys
# sys.stdin = open("CodebaseReplication/PS1_Files/map1.txt")
# startX, startY = map(int, input().split())
# print(startX, startY)

import turtle
from TileStatus import *
from Colors import *

class grid:
    TOPLEFT_X = -300
    TOPLEFT_Y = 0
    SQUARE_SIZE = 30

    def __init__(self, filePath):
        # screen.bgcolor("#a5a5a5")
        turtle.speed(0)
        turtle.tracer(0)
        with open (filePath) as fin:
            startX, startY = map(int, fin.readline().split())
            self.startX = startX
            self.startY = startY
            # print(startX, startY)
            rows, columns = map(int, fin.readline().split())
            self.rows = rows
            self.columns = columns
            board = [list(map(int, fin.readline().split())) for _ in range(rows)]
            # print(*board, sep ='\n')
        self.board = board

    def drawGrid(self, rows, columns):
        color = "filler"
        for i in range(rows):
            for j in range(columns):
                color = self.board[i][j]
                self.drawSquare(i, j, color)
        turtle.update()

    def drawSquare(self, i, j, color):
        turtle.up()
        xLoc = self.TOPLEFT_X + i * self.SQUARE_SIZE
        yLoc = self.TOPLEFT_Y + j * self.SQUARE_SIZE
        turtle.goto(xLoc, yLoc)
        turtle.seth(0)
        turtle.down()
        sColor = Colors.CLEAN
        if color == TileStatus.CLEAN.value:
            sColor = Colors.CLEAN
        if color == TileStatus.DIRTY.value:
            sColor = Colors.DIRTY
        if color == TileStatus.WALL.value:
            sColor = Colors.WALL
        turtle.fillcolor(sColor.value)
        turtle.pencolor("#a5a5a5")
        turtle.begin_fill()
        for _ in range(4):
            turtle.fd(self.SQUARE_SIZE - 2)
            turtle.right(90)
        turtle.end_fill()
    
    def out(self, a, b):
        if a < 0 or a >= self.rows or b < 0 or b >= self.columns:
            return True
        return False
    
    def getSquareStatus(self, i, j):
        if self.out(i, j):
            return -1
        return self.board[i][j]
        
    def getCurrentStatus(self, i, j):
        return self.getSquareStatus(i, j)
    def getLeftStatus(self, i, j):
        return self.getSquareStatus(i, j - 1)
    def getRightStatus(self, i, j):
        return self.getSquareStatus(i, j + 1)
    def getAboveStatus(self, i, j):
        return self.getSquareStatus(i - 1, j)
    def getBelowStatus(self, i, j):
        return self.getSquareStatus(i + 1, j)

# if we press play from this file, the code below will run
if __name__ == "__main__":
    testGrid = grid("CodebaseReplication/PS1_Files/map1.txt")
    testGrid.drawGrid(10, 10)
    
    # could go inside draw grid, then we could take it out of main
    turtle.speed(0)
    turtle.tracer(0)
    screen = turtle.Screen()
    screen.setup(1000, 600)
    screen.exitonclick()

'''
functions: 
drawSquare(x, y, color)
i/o
'''

