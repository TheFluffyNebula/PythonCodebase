import turtle
from Action import *
from TileStatus import *
from Colors import *
import grid

class agent:
    AGENT_COLOR = "#70ad47"

    def __init__(self, x, y, sqSize, grid):
        self.i = 0
        self.j = 0
        self.initX = x
        self.initY = y
        self.sqSize = sqSize
        self.AGENT_SIZE = sqSize / 3
        self.t = turtle.Turtle()
        self.grid = grid

    def drawAgent(self):
        # separate turtle to draw the agent
        self.t.clear()
        self.t.speed(0)

        self.t.up()
        self.t.goto(self.initX + self.i * self.sqSize, self.initY - self.j * self.sqSize - self.AGENT_SIZE)
        self.t.fillcolor(self.AGENT_COLOR)
        self.t.begin_fill()
        self.t.circle(self.AGENT_SIZE)
        self.t.end_fill()

    def getAction(self):
        curStatus = self.grid.getSquareStatus(self.i, self.j)
        leftStatus = self.grid.getSquareStatus(self.i, self.j - 1)
        rightStatus = self.grid.getSquareStatus(self.i, self.j + 1)
        aboveStatus = self.grid.getSquareStatus(self.i - 1, self.j)
        belowStatus = self.grid.getSquareStatus(self.i + 1, self.j)

        if curStatus == TileStatus.DIRTY:
            return Action.CLEAN
        if leftStatus == TileStatus.DIRTY:
            return Action.LEFT
        if rightStatus == TileStatus.DIRTY:
            return Action.RIGHT
        if aboveStatus == TileStatus.DIRTY:
            return Action.UP
        if belowStatus == TileStatus.DIRTY:
            return Action.DOWN
        return Action.DO_NOTHING

    def move(self):
        action = self.getAction()
        if action == Action.CLEAN:
            self.grid.clean(self.i, self.j)
            self.grid.drawSquare(self.i, self.j, Colors.CLEAN)
            return
        if action == Action.LEFT:
            self.j -= 1
        if action == Action.RIGHT:
            self.j += 1
        if action == Action.UP:
            self.i -= 1
        if action == Action.DOWN:
            self.i += 1
        if action == Action.DO_NOTHING:
            return
        # redraw the agent in its new position
        self.drawAgent()
        return


# if we press play from this file, the code below will run
if __name__ == "__main__":
    screen = turtle.Screen()
    
    turtle.speed(0)
    turtle.goto(100, 0)
    turtle.goto(100, 100)
    turtle.goto(0, 100)
    turtle.goto(0, 0)

    board = grid.grid("CodebaseReplication/PS1_Files/map1.txt")
    a = agent(50, 50, 30, board)
    a.drawAgent()

    screen.exitonclick()
