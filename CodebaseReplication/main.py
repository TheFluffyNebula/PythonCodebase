import grid
import agent
import turtle
screen = turtle.Screen()

board = grid.grid("CodebaseReplication/PS1_Files/map1.txt")
board.drawGrid(10, 10)
topLeftX = board.TOPLEFT_X + (board.SQUARE_SIZE / 2)
topLeftY = -topLeftX - board.SQUARE_SIZE
a = agent.agent(topLeftX, topLeftY, board.SQUARE_SIZE, board)

for i in range(5):
    print(i)
    a.move()

board = a.grid
print(board)
nonWall = 0
clean = 0
# TODO: make grid a class and have a method that counts tiles cleaned?
for i in range(board.rows):
    for j in range(board.columns):
        if board.getSquareStatus(i, j) == 0:
            clean += 1
        if board.getSquareStatus(i, j) != 2:
            nonWall += 1
print(f"clean: {clean}/{nonWall}")
print(f"% cleaned: {clean/nonWall}")


screen.exitonclick()


'''
testing
'''
# a.drawAgent(1, 1)
# a.drawAgent(0, 0)

