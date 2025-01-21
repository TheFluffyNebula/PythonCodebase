import turtle
from enum import Enum

class agent:
    AGENT_COLOR = "#70ad47"
    class Action(Enum):
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3
        CLEAN = 4
        DO_NOTHING = 5

    def __init__(self, x, y, sqSize, grid):
        self.i = 0
        self.j = 0
        self.initX = x
        self.initY = y
        self.sqSize = sqSize
        self.AGENT_SIZE = sqSize / 3
        self.t = turtle.Turtle()
        self.grid = grid

    def drawAgent(self, i, j):
        # update the agent's coordinates
        self.i = i
        self.j = j
        # separate turtle to draw the agent
        self.t.clear()
        self.t.speed(0)

        self.t.up()
        self.t.goto(self.initX + i * self.sqSize, self.initY - j * self.sqSize - self.AGENT_SIZE)
        self.t.fillcolor(self.AGENT_COLOR)
        self.t.begin_fill()
        self.t.circle(self.AGENT_SIZE)
        self.t.end_fill()

    def getAction(self):
        curStatus = self.grid.getStatus(self.i, self.j)
        leftStatus = self.grid.getStatus(self.i, self.j - 1)
        rightStatus = self.grid.getStatus(self.i, self.j + 1)
        aboveStatus = self.grid.getStatus(self.i - 1, self.j)
        belowStatus = self.grid.getStatus(self.i + 1, self.j)

        if curStatus == self.grid.TileStatus.DIRTY:
            return self.Action.CLEAN
        if leftStatus == self.grid.TileStatus.DIRTY:
            return self.Action.LEFT
        if rightStatus == self.grid.TileStatus.DIRTY:
            return self.Action.RIGHT
        if aboveStatus == self.grid.TileStatus.DIRTY:
            return self.Action.UP
        if belowStatus == self.grid.TileStatus.DIRTY:
            return self.Action.DOWN
        return self.Action.DO_NOTHING

    def move(self):
        action = self.getAction()
        # if action == self.Action.CLEAN:



# if we press play from this file, the code below will run
if __name__ == "__main__":
    screen = turtle.Screen()
    
    turtle.speed(0)
    turtle.goto(100, 0)
    turtle.goto(100, 100)
    turtle.goto(0, 100)
    turtle.goto(0, 0)

    a = agent(50, 50, 30)
    a.drawAgent(0, 0)

    screen.exitonclick()
