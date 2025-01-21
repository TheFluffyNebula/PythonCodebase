import grid
import agent
import turtle
screen = turtle.Screen()

board = grid.readFile("CodebaseReplication/PS1_Files/map1.txt")
grid.drawGrid(10, 10, board)
topLeftX = grid.TOPLEFT_X + (grid.SQUARE_SIZE / 2)
topLeftY = -topLeftX - grid.SQUARE_SIZE
a = agent.agent(topLeftX, topLeftY, grid.SQUARE_SIZE, board)

for i in range(200):
    a.move()

nonWall = 0
clean = 0
# TODO: make grid a class and have a method that counts tiles cleaned?
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 0:
            clean += 1
print(f"clean: {clean}/{nonWall}")
print(f"percentage: {clean/nonWall}")


screen.exitonclick()


'''
testing
'''
# a.drawAgent(1, 1)
# a.drawAgent(0, 0)

