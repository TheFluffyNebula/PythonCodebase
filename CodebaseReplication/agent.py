import turtle

AGENT_COLOR = "#70ad47"
AGENT_SIZE = 10

def drawAgent(x, y):
    # separate turtle to draw the agent
    t = turtle.Turtle()
    t.speed(0)

    t.up()
    t.goto(x, y - AGENT_SIZE)
    t.fillcolor(AGENT_COLOR)
    t.begin_fill()
    t.circle(AGENT_SIZE)
    t.end_fill()


# if we press play from this file, the code below will run
if __name__ == "__main__":
    screen = turtle.Screen()
    
    turtle.speed(0)
    turtle.goto(100, 0)
    turtle.goto(100, 100)
    turtle.goto(0, 100)
    turtle.goto(0, 0)

    drawAgent(50, 50)

    screen.exitonclick()
