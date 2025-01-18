import grid
import agent
import turtle
screen = turtle.Screen()

board = grid.readFile("CodebaseReplication/PS1_Files/map1.txt")
grid.drawGrid(10, 10, board)
x = (-300 + -270) // 2
y = -x - 30
agent.drawAgent(x, y)

screen.exitonclick()
