# import sys
# sys.stdin = open("CodebaseReplication/PS1_Files/map1.txt")
# startX, startY = map(int, input().split())
# print(startX, startY)

# import copy
# do we have to copy.deepcopy() the board (?)
import turtle
screen = turtle.Screen()
screen.setup(1000, 600)
# screen.bgcolor("#a5a5a5")

turtle.speed(0)
turtle.tracer(0)

TOPLEFT_X = -300
TOPLEFT_Y = 0
SQUARE_SIZE = 30


def readFile(filePath):
    with open (filePath) as fin:
        startX, startY = map(int, fin.readline().split())
        # print(startX, startY)
        rows, columns = map(int, fin.readline().split())
        board = [list(map(int, fin.readline().split())) for _ in range(rows)]
        # print(*board, sep ='\n')
        return board

def drawGrid(rows, columns, board):
    color = "filler"
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 1:
                color = "#f4b083"
            if board[i][j] == 0:
                color = "#000000"
            drawSquare(TOPLEFT_X + i * SQUARE_SIZE, TOPLEFT_Y + j * SQUARE_SIZE, color)


def drawSquare(x, y, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.pencolor("#a5a5a5")
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(SQUARE_SIZE - 2)
        turtle.right(90)
    turtle.end_fill()

board = readFile("CodebaseReplication/PS1_Files/map1.txt")
drawGrid(10, 10, board)
turtle.update()

screen.exitonclick()

'''
functions: 
drawSquare(x, y, color)
i/o
'''

