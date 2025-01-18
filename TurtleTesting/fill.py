import turtle

# turtle.up()
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.goto(100, 0)
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.end_fill()


# prevent turtle from exiting immediately
screen = turtle.Screen()
screen.exitonclick()